from fastapi import APIRouter

from services.patient_twin_service import generate_patient_twin

router = APIRouter(
    prefix="/patients",
    tags=["Patient Twin"]
)


@router.get("/{patient_id}/patient-twin")
def patient_twin(patient_id: int):

    return generate_patient_twin(patient_id)