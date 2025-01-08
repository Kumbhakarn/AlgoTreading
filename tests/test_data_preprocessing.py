import pytest
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    data = load_data('AAPL', '2022-01-01', '2024-01-01', '1m')
    processed_data = preprocess_data(data)
    assert 'RSI' in processed_data.columns
    assert 'MACD' in processed_data.columns
    assert 'Williams %R' in processed_data.columns
    