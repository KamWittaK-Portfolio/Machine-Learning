import os
import pandas as pd
from supabase import create_client, Client
from zenml.steps import step
from dotenv import load_dotenv
from typing import Any

load_dotenv()

def load_data_plain():
    # Load CSV file
    df_csv = pd.read_csv("data/KNNAlgorithmDataset.csv")
    
    # Load environment variables
    URL: str = os.getenv("DB_URL", "")
    KEY: str = os.getenv("DB_KEY", "")

    # Create Supabase client
    supabase: Client = create_client(URL, KEY)

    # Query Supabase table
    response: Any = supabase.table("KNNAlgorithmDataset1").select("*").execute()
    df_supabase = pd.DataFrame(response.data)

    # Combine CSV and Supabase data
    return pd.concat([df_csv, df_supabase], ignore_index=True)

@step
def load_data() -> pd.DataFrame:
    return  load_data_plain()
