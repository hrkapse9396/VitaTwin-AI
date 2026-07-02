from fastapi import APIRouter
from database.database import SessionLocal
from database.models import ECGPrediction


router = APIRouter()


@router.get("/patients/{patient_id}/history")
def get_patient_history(patient_id:int):

    db = SessionLocal()


    records = db.query(
        ECGPrediction
    ).filter(
        ECGPrediction.patient_id == patient_id
    ).all()


    history=[]


    for r in records:

        history.append({

            "prediction": r.prediction,

            "confidence": round(
                r.confidence,
                2
            ),

            "risk_level": r.risk_level

        })


    db.close()


    return {

        "patient_id": patient_id,

        "history": history

    }