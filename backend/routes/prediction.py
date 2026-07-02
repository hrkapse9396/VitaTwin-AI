from fastapi import APIRouter

from schemas.prediction_schema import ECGRequest
from services.prediction_service import predict_afib


router = APIRouter()


@router.post("/predict")
def prediction(request: ECGRequest):

    result = predict_afib(
    request.patient_id,
    request.ecg_data
)

    return result