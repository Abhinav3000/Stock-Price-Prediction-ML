import pandas as pd

def add_features(df):
    df['Target'] = df['Close'].shift(-1)
    df['MA_5'] = df['Close'].rolling(window=5).mean()
    df['MA_10'] = df['Close'].rolling(window=10).mean()
    df = df.dropna()
    return df
