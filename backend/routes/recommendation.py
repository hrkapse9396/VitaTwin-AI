from fastapi import APIRouter

from services.recommendation_service import generate_recommendations

router = APIRouter(
    prefix="/patients",
    tags=["Recommendations"]
)


@router.get("/{patient_id}/recommendations")
def recommendations(patient_id: int):
    return generate_recommendations(patient_id)
