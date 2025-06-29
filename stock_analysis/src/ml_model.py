"""ML model module.

Placeholder for machine learning model training and prediction.
"""

from sklearn.linear_model import LinearRegression


def train_model(features, targets):
    """Train a simple linear regression model."""
    model = LinearRegression()
    model.fit(features, targets)
    return model
