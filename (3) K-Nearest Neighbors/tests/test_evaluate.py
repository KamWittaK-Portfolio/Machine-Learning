import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from steps.evaluate import evaluate_model_plain
from steps.ingest import load_data_plain
from steps.preprocess import clean_scale_plain
from steps.train import fit_model_plain



def test_metrics():
    data = load_data_plain()
    x_train, x_test, y_train, y_test = clean_scale_plain(data)
    model = fit_model_plain(x_train, y_train)
    accuracy = evaluate_model_plain(model, x_test, y_test)

    assert accuracy > 0.8