import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from zenml.steps import step
from src.steps.ingest import load_data

@step
def clean_scale(data: pd.DataFrame) -> list:
    features = ['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']
    
    result = "diagnosis"

    scale = StandardScaler()

    scaled_features = scale.fit_transform(data[features])


    x_train, x_test, y_train, t_test = train_test_split(scaled_features, data[result], train_size=0.8, random_state=42)

    return [x_train, x_test, y_train, t_test]


