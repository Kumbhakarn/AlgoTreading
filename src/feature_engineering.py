import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_features(data):
    """
    Scale the features (RSI, MACD, Williams %R) for machine learning.
    """
    scaler = StandardScaler()
    features = ['RSI', 'MACD', 'Signal', 'Williams %R']
    data[features] = scaler.fit_transform(data[features])
    return data, scaler

def create_target_variable(data, threshold=0.02):
    """
    Create a binary target variable based on price movement.
    Target = 1 if price increases by more than threshold, else 0.
    """
    data['Target'] = np.where(data['Close'].pct_change().shift(-1) > threshold, 1, 0)
    return data