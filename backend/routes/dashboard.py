from fastapi import APIRouter

from database.database import SessionLocal
from database.models import Patient, ECGPrediction


router = APIRouter()


@router.get("/patients/{patient_id}/dashboard")
def patient_dashboard(patient_id: int):

    db = SessionLocal()


    patient = db.query(
        Patient
    ).filter(
        Patient.id == patient_id
    ).first()


    if patient is None:

        db.close()

        return {
            "message": "Patient not found"
        }


    predictions = db.query(
        ECGPrediction
    ).filter(
        ECGPrediction.patient_id == patient_id
    ).order_by(
        ECGPrediction.timestamp.desc()
    ).all()


    history = []


    for record in predictions:

        history.append({

            "prediction": record.prediction,

            "confidence": round(
                record.confidence,
                2
            ),

            "risk_score": round(
                record.risk_score,
                2
            ),

            "risk_level": record.risk_level,

            "date": record.timestamp

        })


    latest_prediction = None


    if len(predictions) > 0:

        latest = predictions[0]

        latest_prediction = {

            "prediction": latest.prediction,

            "confidence": round(
                latest.confidence,
                2
            ),

            "risk_level": latest.risk_level

        }


    db.close()


    return {

        "patient": {

            "id": patient.id,

            "name": patient.name,

            "age": patient.age,

            "gender": patient.gender

        },

        "latest_prediction": latest_prediction,

        "health_summary": {

            "total_predictions": len(history),

            "afib_detected": any(
                item["prediction"] == "AFIB"
                for item in history
            )

        },

        "history": history

    }