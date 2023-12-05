import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_user_input():
    ticker = input("Enter stock ticker symbol: ").upper()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    return ticker, start_date, end_date

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_returns(stock_data):
    stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()
    return stock_data

def calculate_metrics(stock_data):
    average_daily_return = stock_data['Daily_Return'].mean()
    volatility = stock_data['Daily_Return'].std()
    cumulative_return = (stock_data['Adj Close'][-1] / stock_data['Adj Close'][0]) - 1

    return average_daily_return, volatility, cumulative_return

def plot_stock_data(stock_data, ticker):
    plt.figure(figsize=(10, 6))
    stock_data['Adj Close'].plot(label=ticker)
    plt.title(f'{ticker} Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Get user input
    ticker, start_date, end_date = get_user_input()

    # Get stock data
    stock_data = get_stock_data(ticker, start_date, end_date)

    # Calculate daily returns
    stock_data = calculate_returns(stock_data)

    # Calculate financial metrics
    avg_daily_return, volatility, cumulative_return = calculate_metrics(stock_data)

    # Print metrics
    print(f"Average Daily Return: {avg_daily_return:.4f}")
    print(f"Volatility: {volatility:.4f}")
    print(f"Cumulative Return: {cumulative_return:.4f}")

    # Plot stock data
    plot_stock_data(stock_data, ticker)
