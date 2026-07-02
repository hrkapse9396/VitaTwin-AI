import os
from tensorflow.keras.models import load_model


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "afib_cnn_model.h5"
)


def load_afib_model():

    model = load_model(MODEL_PATH)

    return model


model = load_afib_model()

print("AFIB Model Loaded Successfully")