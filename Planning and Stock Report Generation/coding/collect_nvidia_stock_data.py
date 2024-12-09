# filename: collect_nvidia_stock_data.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for Nvidia and the dates for last month
ticker_symbol = "NVDA"
end_date = "2024-04-23"
start_date = "2024-03-23"

# Fetch data from Yahoo Finance
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save the data to a CSV file for analysis
data.to_csv("nvidia_stock_data.csv")

# Print the first few rows of the data to confirm it's correctly retrieved
print(data.head())

# Create a basic plot of the closing prices
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Closing Price')
plt.title(f'Nvidia Stock Closing Prices from {start_date} to {end_date}')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.savefig('nvidia_stock_prices.png')
plt.show()