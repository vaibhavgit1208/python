import pandas as pd
import matplotlib.pyplot as plt

# Load sample time series data (historical stock prices)
# You can replace this with your own time series data
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'StockPrice': [100, 105, 98, 102, 110]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Display the time series data
print("Time Series Data:")
print(df)

# Plot the time series data
df['StockPrice'].plot(title="Stock Price Over Time", xlabel='Date', ylabel='Stock Price')
plt.show()

# Perform basic time series operations
print("Basic Time Series Operations:")
# Calculate the mean stock price
print("Mean Stock Price:", df['StockPrice'].mean())

# Resample the data for monthly average stock price
monthly_data = df['StockPrice'].resample('M').mean()
print("Monthly Mean Stock Prices:")
print(monthly_data)
