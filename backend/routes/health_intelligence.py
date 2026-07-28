from fastapi import APIRouter

from services.health_intelligence_service import (
    generate_health_intelligence
)

router = APIRouter(
    prefix="/patients",
    tags=["Health Intelligence"]
)


@router.get("/{patient_id}/health-intelligence")
def health_intelligence(patient_id: int):

    return generate_health_intelligence(patient_id)