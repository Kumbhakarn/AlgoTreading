import os
import joblib
import logging

def save_model(model, filename):
    """Save the trained model."""
    joblib.dump(model, filename)

def load_model(filename):
    """Load a saved model."""
    return joblib.load(filename)

def setup_logger():
    """Set up logger for the application."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def save_model(model, filename):
    """Save the trained model to the specified file."""
    joblib.dump(model, filename)

def save_preprocess_objects(scaler, filename):
    """Save the preprocessing objects like scaler."""
    joblib.dump(scaler, filename)
