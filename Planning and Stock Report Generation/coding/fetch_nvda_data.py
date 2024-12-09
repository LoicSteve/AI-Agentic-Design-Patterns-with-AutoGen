# filename: fetch_nvda_data.py
import yfinance as yf
import pandas as pd

# Set the date range for the past month
end_date = pd.Timestamp('2024-12-09')  # Today's date
start_date = end_date - pd.DateOffset(months=1)  # One month ago

# Fetch historical stock data for Nvidia
nvda_stock = yf.Ticker("NVDA")
historical_data = nvda_stock.history(start=start_date, end=end_date)

# Print the historical data to review
print(historical_data)