from pydantic import BaseModel


class ECGRequest(BaseModel):

    patient_id: int

    ecg_data: list