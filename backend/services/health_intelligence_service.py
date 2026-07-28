from database.database import SessionLocal
from database.models import ECGPrediction


def generate_health_intelligence(patient_id: int):

    db = SessionLocal()

    try:

        predictions = (

            db.query(ECGPrediction)

            .filter(
                ECGPrediction.patient_id == patient_id
            )

            .order_by(
                ECGPrediction.timestamp.desc()
            )

            .all()

        )

        if len(predictions) == 0:

            return {
                "message": "No prediction history found."
            }

        latest = predictions[0]

        risk_score = latest.risk_score

        if risk_score < 30:

            future_risk = "LOW"

            stability = "STABLE"

            progression = "UNLIKELY"

            follow_up = "6 Months"

        elif risk_score < 70:

            future_risk = "MEDIUM"

            stability = "MODERATE"

            progression = "POSSIBLE"

            follow_up = "1 Month"

        else:

            future_risk = "HIGH"

            stability = "UNSTABLE"

            progression = "LIKELY"

            follow_up = "24 Hours"

        return {

            "future_risk": future_risk,

            "future_risk_score": round(risk_score, 2),

            "cardiac_stability": stability,

            "disease_progression": progression,

            "clinical_priority": latest.risk_level,

            "recommended_follow_up": follow_up

        }

    finally:

        db.close()