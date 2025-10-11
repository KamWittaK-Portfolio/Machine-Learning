from sklearn.neighbors import KNeighborsClassifier
from zenml.steps import step


def fit_model_plain(x_train, y_train):
    model = KNeighborsClassifier()

    model.fit(x_train, y_train)

    return model

@step
def fit_model(x_train, y_train):
    return fit_model_plain(x_train, y_train)