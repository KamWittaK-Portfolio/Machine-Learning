import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from zenml.steps import step

@step
def clean_scale(data: pd.DataFrame) -> list:
    features = ["radius_mean","ttexture_mean","tperimeter_mean","tarea_mean","tsmoothness_mean","tcompactness_mean","tconcavity_mean","tconcave","points_mean","tsymmetry_mean","tfractal_dimension_mean","tradius_se","ttexture_se","tperimeter_se","tarea_se","tsmoothness_se","tcompactness_se","tconcavity_se","tconcave","points_se","tsymmetry_se","tfractal_dimension_se","tradius_worst","ttexture_worst","tperimeter_worst","tarea_worst","tsmoothness_worst","tcompactness_worst","tconcavity_worst","tconcave","points_worst","tsymmetry_worst","tfractal_dimension_worst"]
    result = "diagnosis"

    scale = StandardScaler()

    scaled_features = scale.fit_transform(data[features])

    return train_test_split(scaled_features, data[result], train_size=0.8, random_state=42)
