import pandas as pd
import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.steps.preprocess import clean_scale_plain

def test_mean_var():
    # Create a small fake dataset for testing
    data = pd.DataFrame({
        'radius_mean': np.random.rand(10),
        'texture_mean': np.random.rand(10),
        'perimeter_mean': np.random.rand(10),
        'area_mean': np.random.rand(10),
        'smoothness_mean': np.random.rand(10),
        'compactness_mean': np.random.rand(10),
        'concavity_mean': np.random.rand(10),
        'concave points_mean': np.random.rand(10),
        'symmetry_mean': np.random.rand(10),
        'fractal_dimension_mean': np.random.rand(10),
        'radius_se': np.random.rand(10),
        'texture_se': np.random.rand(10),
        'perimeter_se': np.random.rand(10),
        'area_se': np.random.rand(10),
        'smoothness_se': np.random.rand(10),
        'compactness_se': np.random.rand(10),
        'concavity_se': np.random.rand(10),
        'concave points_se': np.random.rand(10),
        'symmetry_se': np.random.rand(10),
        'fractal_dimension_se': np.random.rand(10),
        'radius_worst': np.random.rand(10),
        'texture_worst': np.random.rand(10),
        'perimeter_worst': np.random.rand(10),
        'area_worst': np.random.rand(10),
        'smoothness_worst': np.random.rand(10),
        'compactness_worst': np.random.rand(10),
        'concavity_worst': np.random.rand(10),
        'concave points_worst': np.random.rand(10),
        'symmetry_worst': np.random.rand(10),
        'fractal_dimension_worst': np.random.rand(10),
        'diagnosis': np.random.randint(0, 2, size=10)
    })

    x_train, x_test, y_train, y_test = clean_scale_plain(data)
    mean, var = np.mean(x_train), np.var(x_train)
    print(mean, var)
    assert abs(round(mean,1)) < 0.2
    assert abs(round(var,1)) > 0.8