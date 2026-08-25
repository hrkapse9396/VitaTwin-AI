from database.database import SessionLocal
from database.models import ECGPrediction


def generate_recommendations(patient_id: int):
    """Generate patient-specific, human-readable recommendations.

    Recommendations are based on the patient's latest ECG result together
    with recent rhythm history, risk trend, and historical risk. This is a
    rule-based health-support layer and is not a medical diagnosis.
    """

    db = SessionLocal()

    try:
        predictions = (
            db.query(ECGPrediction)
            .filter(ECGPrediction.patient_id == patient_id)
            .order_by(ECGPrediction.timestamp.desc())
            .all()
        )

        if not predictions:
            return {
                "monitoring_priority": "LOW",
                "summary": "There is not enough ECG history to generate a patient-specific recommendation.",
                "recommendations": [
                    "Continue regular health monitoring and add future ECG records for better trend analysis."
                ],
            }

        latest = predictions[0]
        previous = predictions[1] if len(predictions) > 1 else None
        recent = predictions[:5]

        latest_risk = float(latest.risk_score or 0)
        previous_risk = float(previous.risk_score or 0) if previous else latest_risk
        risk_change = latest_risk - previous_risk

        if risk_change > 5:
            risk_trend = "INCREASING"
        elif risk_change < -5:
            risk_trend = "DECREASING"
        else:
            risk_trend = "STABLE"

        recent_afib_count = sum(
            1 for item in recent
            if str(item.prediction).upper() == "AFIB"
        )
        recent_count = len(recent)
        afib_frequency = round((recent_afib_count / recent_count) * 100, 1)

        total_afib_count = sum(
            1 for item in predictions
            if str(item.prediction).upper() == "AFIB"
        )

        highest_risk = max(float(item.risk_score or 0) for item in predictions)

        if latest_risk >= 70 or risk_trend == "INCREASING":
            priority = "HIGH"
        elif latest_risk >= 30 or recent_afib_count >= 1:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        recommendations = []

        # Latest ECG interpretation
        if str(latest.prediction).upper() == "AFIB":
            recommendations.append(
                "The latest ECG is classified as AFIB. Arrange prompt clinical review to interpret this result in the context of the patient's symptoms and medical history."
            )
        else:
            recommendations.append(
                "The latest ECG is classified as NORMAL. This is reassuring for the latest recording, but it should be considered together with the patient's previous ECG history."
            )

        # Recent rhythm pattern
        if recent_afib_count > 0:
            recommendations.append(
                f"AFIB was identified in {recent_afib_count} of the {recent_count} most recent ECG records ({afib_frequency}%). Recurring abnormal rhythm results should be reviewed by a healthcare professional."
            )
        else:
            recommendations.append(
                "No AFIB was identified in the five most recent ECG records. Continue routine monitoring so that future changes can be detected."
            )

        # Risk trend
        if risk_trend == "INCREASING":
            recommendations.append(
                f"The recent risk score has increased by {abs(risk_change):.2f} points. Increased monitoring and clinical review are recommended if this pattern continues."
            )
        elif risk_trend == "DECREASING":
            recommendations.append(
                f"The recent risk score has decreased by {abs(risk_change):.2f} points. This is an improving trend, but continued monitoring is recommended because previous abnormal records remain part of the patient's history."
            )
        else:
            recommendations.append(
                "The recent risk score is stable. Continue regular monitoring and compare future ECG results with this history."
            )

        # Longitudinal history
        if highest_risk >= 70 and latest_risk < 70:
            recommendations.append(
                f"The patient's history contains a previous high-risk score of {highest_risk:.2f}. Even though the latest score is lower, future abnormal results should be reviewed rather than considered in isolation."
            )

        if total_afib_count > 0:
            recommendations.append(
                f"The record contains {total_afib_count} AFIB prediction(s) across {len(predictions)} ECG records. Maintaining an updated ECG history will help track whether the pattern is recurring."
            )

        # Follow-up guidance based on the current rule set
        if priority == "HIGH":
            follow_up = "Prompt clinical review"
            summary = "The patient's recent record indicates a higher monitoring priority because of the current risk and/or worsening trend."
        elif priority == "MEDIUM":
            follow_up = "Regular clinical follow-up"
            summary = "The latest risk is not high, but the patient's history contains findings that justify continued monitoring and clinical follow-up."
        else:
            follow_up = "Routine monitoring"
            summary = "The latest record is low risk and the recent history does not show a strong warning pattern. Continue routine monitoring."

        return {
            "monitoring_priority": priority,
            "summary": summary,
            "latest_prediction": str(latest.prediction),
            "latest_risk_score": round(latest_risk, 2),
            "previous_risk_score": round(previous_risk, 2),
            "risk_change": round(risk_change, 2),
            "risk_trend": risk_trend,
            "recent_afib_count": recent_afib_count,
            "recent_prediction_count": recent_count,
            "afib_frequency": afib_frequency,
            "total_afib_count": total_afib_count,
            "total_predictions": len(predictions),
            "highest_historical_risk": round(highest_risk, 2),
            "recommended_follow_up": follow_up,
            "recommendations": recommendations,
        }

    finally:
        db.close()
