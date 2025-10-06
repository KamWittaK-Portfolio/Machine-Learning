# tests/test_ingest.py
import pandas as pd

def test_ingest_schema():
    # Example: replace with your actual ingest function or load CSV
    data = pd.read_csv("data/your_dataset.csv")

    # Check basic sanity
    assert not data.empty, "❌ DataFrame is empty."
    assert len(data) >= 500, "❌ DataFrame has fewer than 500 rows."

    expected_columns = [
        "id", "diagnosis", "radius_mean", "texture_mean", "perimeter_mean", "area_mean",
        "smoothness_mean", "compactness_mean", "concavity_mean", "concave points_mean",
        "symmetry_mean", "fractal_dimension_mean", "radius_se", "texture_se", "perimeter_se",
        "area_se", "smoothness_se", "compactness_se", "concavity_se", "concave points_se",
        "symmetry_se", "fractal_dimension_se", "radius_worst", "texture_worst", "perimeter_worst",
        "area_worst", "smoothness_worst", "compactness_worst", "concavity_worst",
        "concave points_worst", "symmetry_worst", "fractal_dimension_worst", "Unnamed: 32"
    ]

    assert list(data.columns) == expected_columns, "❌ Columns do not match expected schema."
