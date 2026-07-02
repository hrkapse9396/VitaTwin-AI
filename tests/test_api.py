import numpy as np
import requests


X = np.load("datasets/processed/X.npy")


sample = X[83]


ecg_data = sample.tolist()


data = {
    "patient_id": 1,
    "ecg_data": ecg_data
}


response = requests.post(
    "http://127.0.0.1:8000/predict",
    json=data
)


print(response.json())