from zenml.steps import step
from sklearn.metrics import accuracy_score
import mlflow
from mlflow.sklearn import log_model


@step
def evaluate_model_plain(model, X_test, y_test):
    """Evaluates the trained model and logs metrics to MLflow."""
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = float(round(accuracy_score(y_test, y_pred), 2))

    return accuracy

@step
def evaluate_model(model, X_test, y_test):
    # ✅ Set up a valid local MLflow tracking URI
    mlflow.set_tracking_uri("http://localhost:5000")  # or your hosted MLflow server

    # Optional: give it a custom experiment name
    mlflow.set_experiment("KNN_Classification")

    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = float(round(accuracy_score(y_test, y_pred), 2))

    with mlflow.start_run():
        mlflow.log_metric('accuracy', accuracy)
        log_model(model, "model")

    return accuracy
