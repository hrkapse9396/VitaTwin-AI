from database.database import SessionLocal
from database.models import Patient, ECGPrediction


def generate_patient_twin(patient_id: int):

    db = SessionLocal()

    try:

        patient = (

            db.query(Patient)

            .filter(
                Patient.id == patient_id
            )

            .first()

        )

        if patient is None:

            return {

                "error": "Patient not found."

            }

        predictions = (

            db.query(ECGPrediction)

            .filter(
                ECGPrediction.patient_id == patient_id
            )

            .all()

        )

        if len(predictions) == 0:

            return {

                "patient_name": patient.name,

                "message": "No prediction history found."

            }

        total_predictions = len(predictions)

        average_risk = sum(

            p.risk_score

            for p in predictions

        ) / total_predictions

        latest_prediction = predictions[-1].prediction

        highest_risk = max(

            predictions,

            key=lambda x: x.risk_score

        ).risk_level

        health_score = max(

            0,

            round(100 - average_risk, 2)

        )

        if health_score >= 80:

            health_status = "Excellent"

        elif health_score >= 60:

            health_status = "Stable"

        elif health_score >= 40:

            health_status = "Needs Monitoring"

        else:

            health_status = "Critical"

        return {

            "patient_name": patient.name,

            "patient_age": patient.age,

            "patient_gender": patient.gender,

            "total_predictions": total_predictions,

            "average_risk_score": round(

                average_risk,

                2

            ),

            "highest_risk": highest_risk,

            "latest_prediction": latest_prediction,

            "overall_health_score": health_score,

            "health_status": health_status

        }

    finally:

        db.close()