import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from steps.train import fit_model
from steps.ingest import load_data
from steps.preprocess import clean_scale
from steps.evaluate import evaluate_model

def KNN_Classification_Pipeline():
    data = load_data()
    X_train, X_test, y_train, y_test = clean_scale(data)
    model = fit_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
