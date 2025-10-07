import pandas as pd
import numpy as np

def test_mean_var(data: list) -> None:
    x_train, x_test, y_train, y_test = data

    mean, var = np.mean(x_train), np.var(x_train)

    print(f"Mean: {mean}\nVar: {var}")

    assert mean != 0

    assert var != 1