from fastapi import APIRouter, UploadFile, File, Form

from schemas.prediction_schema import ECGRequest
from services.prediction_service import predict_afib, predict_uploaded_ecg

router = APIRouter()


@router.post("/predict")
def prediction(request: ECGRequest):

    result = predict_afib(
        request.patient_id,
        request.ecg_data
    )

    return result


@router.post("/predict/upload")
async def upload_prediction(

    patient_id: int = Form(...),

    file: UploadFile = File(...)

):

    return await predict_uploaded_ecg(
        patient_id,
        file
    )