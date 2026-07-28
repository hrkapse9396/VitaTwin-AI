from database.database import SessionLocal
from database.models import Patient, ECGPrediction

from services.health_intelligence_service import (
    generate_health_intelligence
)

from services.patient_twin_service import (
    generate_patient_twin
)


def generate_report(patient_id: int):

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
                "message": "Patient not found."
            }

        history = (

            db.query(ECGPrediction)

            .filter(
                ECGPrediction.patient_id == patient_id
            )

            .order_by(
                ECGPrediction.timestamp.desc()
            )

            .all()

        )

        if len(history) == 0:

            return {
                "message": "No ECG history found."
            }

        latest = history[0]

        health_intelligence = generate_health_intelligence(
            patient_id
        )

        patient_twin = generate_patient_twin(
            patient_id
        )

        report = {

            "patient": {

                "name": patient.name,

                "age": patient.age,

                "gender": patient.gender

            },

            "latest_prediction": {

                "prediction": latest.prediction,

                "confidence": latest.confidence,

                "risk_score": latest.risk_score,

                "risk_level": latest.risk_level

            },

            "health_intelligence":

                health_intelligence,

            "patient_twin":

                patient_twin,

            "prediction_history": [

                {

                    "prediction": p.prediction,

                    "confidence": p.confidence,

                    "risk_score": p.risk_score,

                    "timestamp": p.timestamp

                }

                for p in history

            ]

        }

        return report

    finally:

        db.close()