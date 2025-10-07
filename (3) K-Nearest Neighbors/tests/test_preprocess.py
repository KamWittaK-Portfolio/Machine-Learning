import pandas as pd
import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.steps.ingest import load_data
from src.steps.preprocess import clean_scale

def test_mean_var():
    data = load_data()
    x_train, x_test, y_train, y_test = clean_scale(data)  # plain function
    mean, var = np.mean(x_train), np.var(x_train)
    
    assert abs(round(mean,1)) == 0
    assert abs(round(var,1)) == 1