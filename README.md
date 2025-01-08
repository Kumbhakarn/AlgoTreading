# Algorithmic Trading System

This is an algorithmic trading system designed to analyze the top 10 stocks of the market at 9:40 AM using real-time data. The system calculates key technical indicators such as MACD, RSI, and VWAP, and makes trading predictions based on these indicators. The prediction can be a recommendation to **Buy**, **Sell**, or **Hold** a stock at the given time.

## Features

- **Real-Time Stock Data Fetching**: Collects minute-level data for top 10 stocks.
- **Technical Indicator Calculation**: Computes key indicators such as MACD, RSI, and VWAP.
- **Prediction Logic**: Makes buy/sell/hold decisions based on the indicators.
- **Scheduled Execution**: Runs the analysis at exactly 9:40 AM.
- **Logging**: Tracks system activities and predictions in log files.

## Prerequisites

- Python 3.8 or later
- Required libraries (listed in `requirements.txt`)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/algorithmic-trading-system.git
    cd algorithmic-trading-system
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Running the Trading System**:
    The main script `main.py` will automatically wait until 9:40 AM and then fetch real-time data for the top 10 stocks, calculate technical indicators, and make predictions.

    To start the system:
    ```bash
    python main.py
    ```

2. **Indicator Calculations**:
    - **MACD (Moving Average Convergence Divergence)**: Measures the relationship between short-term and long-term moving averages.
    - **RSI (Relative Strength Index)**: Measures the speed and change of price movements to identify overbought or oversold conditions.
    - **VWAP (Volume-Weighted Average Price)**: A measure of the average price a stock has traded at throughout the day, based on both volume and price.

3. **Prediction Logic**:
    - **Buy**: If MACD is above the signal line, RSI is below 30 (indicating oversold conditions), and the price is below the VWAP.
    - **Sell**: If MACD is below the signal line, RSI is above 70 (indicating overbought conditions), and the price is above the VWAP.
    - **Hold**: If none of the conditions are met.

## Example Output

Once the system runs, it will print trading predictions for each of the top 10 stocks:

