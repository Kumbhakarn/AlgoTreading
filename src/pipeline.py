import os
import joblib
import pandas as pd
from datetime import datetime
from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import scale_features, create_target_variable
from src.model import build_model, train_model
from src.evaluate import evaluate_model
from src.utils import save_model, save_preprocess_objects
import logging

# Setup logger
logger = logging.getLogger(__name__)

def run_pipeline(symbol, start_date, end_date, interval='1m'):
    """Run the complete machine learning pipeline."""
    logger.info(f"Running pipeline for {symbol} from {start_date} to {end_date}.")

    # Step 1: Load raw data
    logger.info("Loading raw data...")
    raw_data = load_data(symbol, start_date, end_date, interval)
    
    # Step 2: Save raw data
    raw_data_path = os.path.join('data', 'raw', f'{symbol}_raw_data.csv')
    raw_data.to_csv(raw_data_path)
    logger.info(f"Raw data saved at {raw_data_path}")

    # Step 3: Preprocess data (Calculate indicators, clean missing values, etc.)
    logger.info("Preprocessing data...")
    preprocessed_data = preprocess_data(raw_data)
    
    # Step 4: Save preprocessed data
    processed_data_path = os.path.join('artifacts', 'processed', f'{symbol}_preprocessed.csv')
    preprocessed_data.to_csv(processed_data_path)
    logger.info(f"Preprocessed data saved at {processed_data_path}")
    
    # Step 5: Feature engineering (scale features and create target)
    logger.info("Feature engineering...")
    preprocessed_data, scaler = scale_features(preprocessed_data)
    preprocessed_data = create_target_variable(preprocessed_data)
    
    # Save preprocessing objects (scaler, etc.)
    preprocess_path = os.path.join('artifacts', 'preprocess.pkl')
    joblib.dump(scaler, preprocess_path)
    logger.info(f"Preprocessing objects saved at {preprocess_path}")

    # Step 6: Train model
    features = ['RSI', 'MACD', 'Signal', 'Williams %R']
    target = 'Target'
    
    X = preprocessed_data[features].values
    y = preprocessed_data[target].values

    # Split data into train/test
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and train model
    logger.info("Training model...")
    model = build_model(X_train.shape[1])
    model, history = train_model(model, X_train, y_train, X_test, y_test)
    
    # Step 7: Save the trained model
    model_path = os.path.join('artifacts', 'model.pkl')
    save_model(model, model_path)
    logger.info(f"Trained model saved at {model_path}")

    # Step 8: Evaluate the model
    logger.info("Evaluating model...")
    evaluate_model(model, X_test, y_test)
    
    logger.info("Pipeline completed successfully.")

# Example run of the pipeline (for symbol AAPL)
if __name__ == "__main__":
    symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2024-01-01'
    run_pipeline(symbol, start_date, end_date)