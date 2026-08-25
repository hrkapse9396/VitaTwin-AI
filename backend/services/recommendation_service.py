from database.database import SessionLocal
from database.models import ECGPrediction, Patient


def _risk_band(risk_score):
    if risk_score is None:
        return "UNKNOWN"
    if risk_score < 30:
        return "LOW"
    if risk_score < 70:
        return "MEDIUM"
    return "HIGH"


def _build_recommendations(latest, predictions):
    latest_risk = float(latest.risk_score or 0)
    latest_prediction = (latest.prediction or "UNKNOWN").upper()
    recent = predictions[:5]
    recent_afib_count = sum(
        1 for item in recent if (item.prediction or "").upper() == "AFIB"
    )
    recent_count = len(recent)
    afib_frequency = round((recent_afib_count / recent_count) * 100, 1) if recent_count else 0

    previous_risk = None
    if len(predictions) > 1:
        previous_risk = float(predictions[1].risk_score or 0)

    risk_change = round(latest_risk - previous_risk, 2) if previous_risk is not None else None
    if risk_change is None:
        risk_trend = "INSUFFICIENT HISTORY"
    elif risk_change > 5:
        risk_trend = "INCREASING"
    elif risk_change < -5:
        risk_trend = "DECREASING"
    else:
        risk_trend = "STABLE"

    priority = "LOW"
    if latest_risk >= 70 or risk_trend == "INCREASING" or recent_afib_count >= 3:
        priority = "HIGH"
    elif latest_risk >= 30 or recent_afib_count > 0:
        priority = "MEDIUM"

    recommendations = []

    if latest_prediction == "AFIB":
        recommendations.append({
            "type": "CURRENT_RESULT",
            "title": "Abnormal rhythm detected",
            "message": "Your latest ECG record is marked as AFIB. This result should be reviewed with a qualified healthcare professional rather than interpreted on its own."
        })
    elif latest_prediction == "NORMAL":
        recommendations.append({
            "type": "CURRENT_RESULT",
            "title": "Latest rhythm appears normal",
            "message": "Your latest ECG record is marked as NORMAL. Continue routine monitoring because one normal reading does not describe your complete cardiac history."
        })
    else:
        recommendations.append({
            "type": "CURRENT_RESULT",
            "title": "Review the latest result",
            "message": "The latest ECG result should be reviewed together with your previous records to understand your cardiac pattern."
        })

    if risk_trend == "INCREASING":
        recommendations.append({
            "type": "RISK_TREND",
            "title": "Risk trend needs attention",
            "message": "Your latest risk score is higher than the previous recorded score. Continued monitoring and professional follow-up are recommended, especially if this pattern continues."
        })
    elif risk_trend == "DECREASING":
        recommendations.append({
            "type": "RISK_TREND",
            "title": "Risk trend is improving",
            "message": "Your latest risk score is lower than the previous recorded score. This is an encouraging trend, but regular monitoring should continue."
        })
    elif risk_trend == "STABLE":
        recommendations.append({
            "type": "RISK_TREND",
            "title": "Risk trend is stable",
            "message": "Your recent risk scores are relatively stable. Continue regular monitoring so that meaningful changes can be identified over time."
        })

    if recent_afib_count > 0:
        recommendations.append({
            "type": "RHYTHM_PATTERN",
            "title": "Recent AFIB pattern detected",
            "message": f"AFIB appears in {recent_afib_count} of your {recent_count} most recent ECG records ({afib_frequency}%). Repeated or recurring abnormal results should be discussed with a healthcare professional."
        })
    else:
        recommendations.append({
            "type": "RHYTHM_PATTERN",
            "title": "No recent AFIB records",
            "message": "No AFIB result appears in the most recent ECG records reviewed. Continue monitoring so future changes can be identified."
        })

    if priority == "HIGH":
        follow_up_message = "Your current record indicates a higher monitoring priority. Arrange professional medical review promptly, particularly if abnormal results or concerning symptoms are present."
    elif priority == "MEDIUM":
        follow_up_message = "Your record indicates that continued cardiac monitoring is appropriate. Consider professional follow-up if abnormal results recur or symptoms are concerning."
    else:
        follow_up_message = "Your current record indicates a lower monitoring priority. Continue routine monitoring and keep your ECG history updated."

    recommendations.append({
        "type": "FOLLOW_UP",
        "title": "Recommended next step",
        "message": follow_up_message
    })

    recommendations.append({
        "type": "SAFETY",
        "title": "When to seek urgent help",
        "message": "If you experience severe or persistent chest pain, severe shortness of breath, fainting, or other emergency symptoms, seek urgent medical care rather than relying on this system."
    })

    summary = (
        f"Your latest ECG is {latest_prediction} with a {latest_risk:.2f} risk score. "
        f"The recent risk trend is {risk_trend.lower()} and {recent_afib_count} of the last {recent_count} ECG records show AFIB. "
        f"Current monitoring priority is {priority.lower()}."
    )

    return {
        "summary": summary,
        "monitoring_priority": priority,
        "latest_prediction": latest_prediction,
        "latest_risk_score": round(latest_risk, 2),
        "latest_risk_level": latest.risk_level,
        "previous_risk_score": previous_risk,
        "risk_change": risk_change,
        "risk_trend": risk_trend,
        "recent_afib_count": recent_afib_count,
        "recent_prediction_count": recent_count,
        "afib_frequency": afib_frequency,
        "recommendations": recommendations,
        "disclaimer": "These recommendations are generated from stored ECG prediction data and are intended for monitoring support, not diagnosis or treatment."
    }


def generate_recommendations(patient_id: int):
    db = SessionLocal()
    try:
        patient = db.query(Patient).filter(Patient.id == patient_id).first()
        if patient is None:
            return {"message": "Patient not found."}

        predictions = (
            db.query(ECGPrediction)
            .filter(ECGPrediction.patient_id == patient_id)
            .order_by(ECGPrediction.timestamp.desc())
            .all()
        )

        if not predictions:
            return {
                "patient_id": patient_id,
                "patient_name": patient.name,
                "message": "No ECG prediction history is available yet.",
                "monitoring_priority": "LOW",
                "recommendations": [
                    {
                        "type": "BASELINE",
                        "title": "Build a cardiac baseline",
                        "message": "No ECG prediction history is available for this patient. Add an ECG record to begin longitudinal cardiac monitoring."
                    }
                ],
                "disclaimer": "These recommendations are generated from stored ECG prediction data and are intended for monitoring support, not diagnosis or treatment."
            }

        result = _build_recommendations(predictions[0], predictions)
        result["patient_id"] = patient_id
        result["patient_name"] = patient.name
        result["generated_from_records"] = len(predictions)
        return result
    finally:
        db.close()
