import os
import pandas as pd
from sqlalchemy import create_engine
from zenml.steps import step
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")

@step
def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/KNNAlgorithmDataset.csv")

    engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@localhost/knn")
    myresult = df = pd.read_sql("SELECT * FROM knnalgorithmdataset", engine)

    return pd.concat([df, myresult])