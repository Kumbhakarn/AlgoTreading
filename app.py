import streamlit as st
import yfinance as yf
from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import scale_features, create_target_variable
from src.model import train_model
from src.evaluate import evaluate_model

def main():
    st.title("Stock Trading Signal Predictor")

    # User input for stock symbol
    symbol = st.text_input("Enter Stock Symbol", "AAPL")
    if symbol:
        data = load_data(symbol, '2022-01-01', '2024-01-01', '1m')
        data = preprocess_data(data)
        data, scaler = scale_features(data)
        data = create_target_variable(data)

        # Select features and target variable
        features = ['RSI', 'MACD', 'Signal', 'Williams %R']
        target = 'Target'

        # Train model
        model, history = train_model(data, features, target)

        # Make predictions
        X = data[features].values
        predictions = model.predict(X)
        st.write("Buy/Sell Predictions:", predictions)

        # Evaluate model
        evaluate_model(model, X, data[target].values)

if __name__ == "__main__":
    main()