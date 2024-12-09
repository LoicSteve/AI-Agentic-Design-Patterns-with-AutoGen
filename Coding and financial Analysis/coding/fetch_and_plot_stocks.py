# filename: fetch_and_plot_stocks.py
from functions import get_stock_prices, plot_stock_prices
import pandas as pd

# Define the stock symbols and the period
stock_symbols = ['NVDA', 'TSLA']
start_date = '2024-01-01'
end_date = '2024-12-09'

# Fetch the stock prices
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Plot the stock prices and save to a file
plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')