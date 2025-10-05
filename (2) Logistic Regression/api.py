import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Input schema
class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# FastAPI app
app = FastAPI(
    title="Diabetes Prediction API",
    description="Predict diabetes likelihood based on health data",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Diabetes Prediction API is running"}

@app.post("/v1/predict/diabetes")
def predict_diabetes(data: DiabetesInput):
    try:
        input_data = pd.DataFrame([[data.Pregnancies, data.Glucose, data.BloodPressure, data.SkinThickness, data.Insulin, data.BMI, data.DiabetesPedigreeFunction, data.Age]])
        data_scaled = scaler.transform(input_data)
        prediction = model.predict(data_scaled)
        probability = model.predict_proba(data_scaled)[0][1]

        return {
            "status": 200,
            "prediction": bool(prediction[0]),
            "probability": round(float(probability), 3)
        }
    except Exception as e:
        return {"status": 500, "error": str(e)}
