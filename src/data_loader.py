import yfinance as yf
import pandas as pd

def fetch_data(ticker="^GSPC", period="max", save_path="data/sp500.csv"):
    sp500 = yf.Ticker(ticker)
    data = sp500.history(period=period)
    data.to_csv(save_path)
    return data
