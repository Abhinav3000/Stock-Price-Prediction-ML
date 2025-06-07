import joblib
import pandas as pd

def load_model(model_path='models/random_forest.pkl'):
    return joblib.load(model_path)

def predict_next_day(df, model):
    features = ['Close', 'MA_5', 'MA_10']
    latest = df[features].iloc[[-1]]  # 🔥 stylish fix
    return model.predict(latest)[0]
