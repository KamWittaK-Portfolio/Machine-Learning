import os
from src.steps.addKwarg import update_artifact_store_client_kwargs


update_artifact_store_client_kwargs(new_client_kwargs={"endpoint_url": os.getenv("ARTIFACT_URL"), "region_name": "us-east-2",}, store_name="Supabase", store_id=None)