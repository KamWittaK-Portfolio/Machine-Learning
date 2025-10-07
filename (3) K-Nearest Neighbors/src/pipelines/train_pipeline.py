import os
from zenml.pipelines import pipeline
from src.steps.ingest import load_data
#from src.steps.addKwarg import update_artifact_store_client_kwargs




# Step 2: Define the pipeline
@pipeline
def training_pipeline():
    data = load_data()
