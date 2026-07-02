from fastapi import APIRouter
import numpy as np
import os


router = APIRouter()


# Location of ECG dataset
ECG_PATH = "../datasets/processed/X.npy"


@router.get("/patients/{patient_id}/ecg")
def get_patient_ecg(patient_id: int):

    try:

        # Load ECG dataset
        X = np.load(ECG_PATH)


        # Select ECG sample
        # For now patient_id decides sample index
        ecg_signal = X[patient_id - 1]


        # Convert numpy array to list
        ecg_signal = ecg_signal.flatten().tolist()


        return {

            "patient_id": patient_id,

            "length": len(ecg_signal),

            "ecg": ecg_signal[:1250]

        }


    except Exception as e:

        return {

            "error": str(e)

        }