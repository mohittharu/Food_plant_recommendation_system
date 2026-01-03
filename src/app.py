from fastapi import FastAPI
from pydantic import BaseModel
from main import predict

app = FastAPI(title="Food Plant Recommendation API")

class InputData(BaseModel):
    ph: float
    soil_ec: float
    phosphorus: float
    potassium: float
    tsp: float

@app.post("/predict")
def predict_crop(data: InputData):
    input_list = [
        data.ph,
        data.soil_ec,
        data.phosphorus,
        data.potassium,
        data.tsp
    ]

    prediction, confidence = predict(input_list)

    return {
        "prediction": str(prediction),
        "confidence": confidence
    }
