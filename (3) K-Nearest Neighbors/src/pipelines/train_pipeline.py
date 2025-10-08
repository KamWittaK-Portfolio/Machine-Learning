import os
from zenml.pipelines import pipeline
from src.steps.ingest import load_data
from src.steps.preprocess import clean_scale



# Step 2: Define the pipeline
@pipeline
def training_pipeline():
    data = load_data()
    x = clean_scale(data)
