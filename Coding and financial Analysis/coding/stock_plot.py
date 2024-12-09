# filename: stock_plot.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    # Fetches historical stock data
    return yf.download(ticker, start=start_date, end=end_date)

def calculate_ytd_gains(df):
    # Computes YTD gains from the stock dataframe
    initial_price = df.iloc[0]['Adj Close']
    df['YTD Gain'] = (df['Adj Close'] - initial_price) / initial_price * 100
    return df

def plot_stocks(df_nvda, df_tsla):
    plt.figure(figsize=(10, 5))
    plt.plot(df_nvda.index, df_nvda['YTD Gain'], label='NVDA YTD Gain %')
    plt.plot(df_tsla.index, df_tsla['YTD Gain'], label='TSLA YTD Gain %')
    plt.title('YTD Stock Gains for NVDA and TSLA')
    plt.xlabel('Date')
    plt.ylabel('Gain %')
    plt.legend()
    plt.grid(True)
    plt.savefig('ytd_stock_gains.png')
    plt.show()

def main():
    start_date = '2024-01-01'
    end_date = '2024-12-09'  # adjust end_date if required
    nvda_data = fetch_stock_data('NVDA', start_date, end_date)
    tsla_data = fetch_stock_data('TSLA', start_date, end_date)
    
    nvda_data = calculate_ytd_gains(nvda_data)
    tsla_data = calculate_ytd_gains(tsla_data)
    
    plot_stocks(nvda_data, tsla_data)
    
if __name__ == "__main__":
    main()