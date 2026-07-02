from fastapi import APIRouter

from database.database import SessionLocal
from database.models import ECGPrediction

import numpy as np

from services.explanation_service import generate_explanation


router = APIRouter(
    prefix="/patients",
    tags=["Explanation"]
)


ECG_PATH = "../datasets/processed/X.npy"



@router.get("/{patient_id}/explanation")
def get_explanation(patient_id:int):


    db = SessionLocal()



    try:


        # Get latest prediction from database

        latest_prediction = (

            db.query(ECGPrediction)

            .filter(
                ECGPrediction.patient_id == patient_id
            )

            .order_by(
                ECGPrediction.timestamp.desc()
            )

            .first()

        )



        if latest_prediction is None:


            return {

                "error":
                "No prediction found for patient"

            }



        # Load ECG signal

        X = np.load(
            ECG_PATH
        )



        ecg_signal = X[
            patient_id-1
        ]



        ecg_signal = (
            ecg_signal
            .flatten()
            .tolist()
        )



        ecg_signal = ecg_signal[:1250]



        # Generate only explanation

        explanation = generate_explanation(
            ecg_signal
        )



        # Replace model prediction
        # with database prediction

        explanation["prediction"] = (
            latest_prediction.prediction
        )


        explanation["confidence"] = (
            latest_prediction.confidence
        )


        explanation["risk_level"] = (
            latest_prediction.risk_level
        )


        explanation["patient_id"] = (
            patient_id
        )



        return explanation



    finally:


        db.close()