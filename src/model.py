import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import os
import numpy as np  

def train_model(df, save_path='models/random_forest.pkl'):
    features = ['Close', 'MA_5', 'MA_10']
    target = 'Target'
    
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = False)
    
    model = RandomForestRegressor(n_estimators = 50, max_depth = 10, random_state = 42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    # The fixed RMSE calc
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    print(f"Model trained. RMSE: {rmse:.2f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, save_path)
