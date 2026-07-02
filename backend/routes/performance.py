from fastapi import APIRouter

from services.model_evaluation import evaluate_model



router = APIRouter(
    prefix="/performance",
    tags=["Model Performance"]
)





@router.get("/")
def get_model_performance():


    return evaluate_model()