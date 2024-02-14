'''
Creating a Stock Market Analyzer involves several steps, including data collection, analysis, visualization, 
and possibly making predictions using historical stock price data. Here's a step-by-step guide to get you started
with Python3, using Pandas for data manipulation and Matplotlib for data visualization.

To access data for Indian companies using yfinance, you need to use the correct ticker symbols that 
Yahoo Finance uses for stocks listed on Indian stock exchanges like the Bombay Stock Exchange (BSE) and 
the National Stock Exchange of India (NSE). These tickers usually have a suffix that indicates the exchange.

For companies listed on the NSE, the suffix is .NS, and for those on the BSE, it's .BO. 
For example, if you want to fetch data for Reliance Industries Limited, which is listed on the NSE, you would use the ticker symbol RELIANCE.NS.

Here's how you can modify the script to fetch and display data for an Indian company listed on the NSE:
'''

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for an Indian company (e.g., Reliance Industries)
tickerSymbol = 'RELIANCE.NS'  # Use '.NS' for NSE listed companies

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-1-1')

# Calculate the 50-day and 200-day moving averages
tickerDf['MA50'] = tickerDf['Close'].rolling(window=50).mean()
tickerDf['MA200'] = tickerDf['Close'].rolling(window=200).mean()

# Plotting
plt.figure(figsize=(14,7))
plt.plot(tickerDf['Close'], label='Close Price')
plt.plot(tickerDf['MA50'], label='50 Day MA')
plt.plot(tickerDf['MA200'], label='200 Day MA')
plt.title(f'{tickerSymbol} Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
