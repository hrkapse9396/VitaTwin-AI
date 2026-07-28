from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from services.pdf_report_service import generate_pdf_report

router = APIRouter(
    prefix="/patients",
    tags=["PDF Report"]
)


@router.get("/{patient_id}/report/pdf")
def download_pdf(patient_id: int):

    pdf_file = generate_pdf_report(patient_id)

    if pdf_file is None:

        raise HTTPException(
            status_code=404,
            detail="Patient or prediction history not found."
        )

    return FileResponse(
        path=pdf_file,
        filename=f"VitaTwin_Report_Patient_{patient_id}.pdf",
        media_type="application/pdf"
    )