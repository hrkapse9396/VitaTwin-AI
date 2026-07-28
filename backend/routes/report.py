from fastapi import APIRouter

from services.report_service import generate_report

router = APIRouter(

    prefix="/patients",

    tags=["Report"]

)


@router.get("/{patient_id}/report")
def report(patient_id: int):

    return generate_report(patient_id)