# filename: analyze_nvidia_stock_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
data = pd.read_csv('nvidia_stock_data.csv', index_col='Date', parse_dates=True)

# Calculate the daily percentage change
data['Pct Change'] = data['Close'].pct_change() * 100

# Identify days with significant changes (more than 5% change)
significant_changes = data[abs(data['Pct Change']) > 5]

# Creating a visual plot with highlighted days of significant change
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Closing Price')
plt.scatter(significant_changes.index, significant_changes['Close'], color='red', label='Significant Change (>5%)') # mark significant days
plt.title('Nvidia Stock Closing Prices with Significant Changes')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.savefig('nvidia_stock_analysis.png')
plt.show()

# Save the significant changes to a CSV for further reference
significant_changes.to_csv('nvidia_significant_changes.csv')

# Output the significant changes for review
print(significant_changes)