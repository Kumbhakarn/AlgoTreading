import yfinance as yf
import pandas as pd
from config import config

def load_data(symbol, start_date, end_date, interval):
    """
    Load stock data using yfinance.
    """
    data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
    return data

def preprocess_data(data):
    """
    Clean and preprocess the data for model training.
    """
    # Drop rows with missing values
    data = data.dropna()
    
    # Add technical indicators
    data['RSI'] = calculate_rsi(data['Close'])
    data['MACD'], data['Signal'] = calculate_macd(data['Close'])
    data['Williams %R'] = calculate_williams_r(data)

    return data

def calculate_rsi(series, period=14):
    """Calculate Relative Strength Index (RSI)."""
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(series, fast_period=12, slow_period=26, signal_period=9):
    """Calculate MACD and Signal Line."""
    fast_ema = series.ewm(span=fast_period, adjust=False).mean()
    slow_ema = series.ewm(span=slow_period, adjust=False).mean()
    macd = fast_ema - slow_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd, signal

def calculate_williams_r(data, period=14):
    """Calculate Williams %R."""
    high_max = data['High'].rolling(window=period).max()
    low_min = data['Low'].rolling(window=period).min()
    williams_r = -100 * ((high_max - data['Close']) / (high_max - low_min))
    return williams_r