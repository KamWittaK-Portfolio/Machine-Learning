from zenml.pipelines import pipeline
from src.steps.ingest import load_data

@pipeline
def training_pipeline():
    data = load_data()
    