from database.database import SessionLocal
from database.models import ECGPrediction

import numpy as np

from model.model_loader import model
from fastapi import UploadFile

async def predict_uploaded_ecg(
    patient_id: int,
    file: UploadFile
):

    contents = await file.read()

    text = contents.decode("utf-8")

    ecg_data = []

    try:

        for line in text.splitlines():

            line = line.strip()

            if line == "":
                continue

            ecg_data.append(float(line))

    except ValueError:

        return {
            "error": "Invalid ECG file."
        }

    if len(ecg_data) != 1250:

        return {
            "error": "ECG file must contain exactly 1250 samples."
        }

    return predict_afib(
        patient_id,
        ecg_data
    )

    return predict_afib(

        patient_id,

        ecg_data

    )


def predict_afib(patient_id, ecg_data):

    ecg_array = np.array(ecg_data)


    ecg_array = ecg_array.reshape(
        1,
        1250,
        1
    )


    prediction = model.predict(ecg_array)


    probability = float(prediction[0][0])


    if probability >= 0.5:

        result = "AFIB"

    else:

        result = "NORMAL"



    risk_score = probability * 100



    if risk_score < 30:

        risk = "LOW RISK"


    elif risk_score < 70:

        risk = "MEDIUM RISK"


    else:

        risk = "HIGH RISK"



        # Save prediction into database

    db = SessionLocal()


    prediction_record = ECGPrediction(

        patient_id=patient_id,

        prediction=result,

        confidence=probability * 100,

        risk_score=risk_score,

        risk_level=risk

    )


    db.add(prediction_record)

    db.commit()

    db.close()


    return {
        "prediction": result,
        "confidence": round(probability*100,2),
        "risk_score": round(risk_score,2),
        "risk_level": risk
    }
