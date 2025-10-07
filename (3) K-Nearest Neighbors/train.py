from src.pipelines.train_pipeline import training_pipeline

from src.steps.addKwarg import update_artifact_store_client_kwargs
import os



if __name__ == "__main__":
    update_artifact_store_client_kwargs(new_client_kwargs={"endpoint_url": os.getenv("ARTIFACT_URL"), "region_name": "us-east-2",}, store_name="Supabase", store_id=None)
    training_pipeline()