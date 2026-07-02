from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes.prediction import router as prediction_router
from routes.history import router as history_router
from routes.dashboard import router as dashboard_router
from routes.ecg import router as ecg_router
from routes.performance import router as performance_router
from routes.patient import router as patient_router
from routes.explanation import router as explanation_router

app = FastAPI()



app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



@app.get("/")
def home():

    return {
        "message":
        "VitaTwin AI Backend Running Successfully"
    }



app.include_router(prediction_router)

app.include_router(history_router)

app.include_router(dashboard_router)

app.include_router(ecg_router)

app.include_router(performance_router)

app.include_router(patient_router)

app.include_router(explanation_router)