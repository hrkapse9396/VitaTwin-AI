from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from services.upload_service import process_ecg_file
from services.prediction_service import predict_afib

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/ecg")
async def upload_ecg(
    patient_id: int = Form(...),
    file: UploadFile = File(...)
):

    try:

        ecg_signal = process_ecg_file(
            file.file,
            file.filename
        )

        result = predict_afib(
            patient_id,
            ecg_signal
        )

        return {
            "status": "success",
            "patient_id": patient_id,
            "samples": len(ecg_signal),
            "prediction": result
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )