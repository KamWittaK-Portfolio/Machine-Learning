from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Import model and scalar
model = joblib.load("insurance_model.pkl")
scalar = joblib.load("scaler.pkl")

# Initialize FastAPI app
app = FastAPI(
    title="Insurance Expense Prediction API",
    description="Predict insurance expenses based on demographic and health data",
    version="1.0"
)

# Define the object that the FastAPI endpoint will expect in a POST request
class InsuranceInput(BaseModel):
    age: int
    sex: int
    bmi: float
    children: int
    smoker: int
    region_northwest: int
    region_southeast: int
    region_southwest: int

# Create API endpoint
@app.post('/v1/predict/insurance')
def predict(data: InsuranceInput):
    input_data = pd.DataFrame([[data.age, data.sex, data.bmi, data.children, data.smoker, data.region_northwest, data.region_southeast, data.region_southwest]])
    input_scaled = scalar.transform(input_data)

    prediction = model.predict(input_scaled)

    return {
        "status": 200,
        "predicted": round(float(prediction), 2)
    }