import os
import pandas as pd
from supabase import create_client, Client
from zenml.steps import step
from dotenv import load_dotenv
from typing import Any

load_dotenv()

@step
def load_data() -> pd.DataFrame:
    # Load CSV file
    df_csv = pd.read_csv("data/KNNAlgorithmDataset.csv")
    
    # Load environment variables
    URL: str = os.getenv("URL", "")
    KEY: str = os.getenv("KEY", "")

    # Create Supabase client
    supabase: Client = create_client(URL, KEY)

    # Query Supabase table
    response: Any = supabase.table("KNNAlgorithmDataset1").select("*").execute()
    df_supabase = pd.DataFrame(response.data)

    print(len(response.data))
    print(response.data[:5])

    # Combine CSV and Supabase data
    return pd.concat([df_csv, df_supabase], ignore_index=True)
