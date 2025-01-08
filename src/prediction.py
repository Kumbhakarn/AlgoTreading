def predict_trade_decision(data):
    """Make a simple buy/sell decision based on MACD, RSI, and VWAP."""
    predictions = {}
    
    for stock, stock_data in data.items():
        macd = stock_data['MACD'].iloc[0]
        macd_signal = stock_data['MACD_signal'].iloc[0]
        rsi = stock_data['RSI'].iloc[0]
        vwap = stock_data['VWAP'].iloc[0]
        close_price = stock_data['Close'].iloc[0]
        
        # Buy if MACD is above the signal line, RSI is below 30 (oversold), and price is below VWAP
        if macd > macd_signal and rsi < 30 and close_price < vwap:
            predictions[stock] = 'Buy'
        
        # Sell if MACD is below the signal line, RSI is above 70 (overbought), and price is above VWAP
        elif macd < macd_signal and rsi > 70 and close_price > vwap:
            predictions[stock] = 'Sell'
        
        # No action if none of the conditions are met
        else:
            predictions[stock] = 'Hold'
    
    return predictions
