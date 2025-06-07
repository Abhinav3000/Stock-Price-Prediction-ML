from src.data_loader import fetch_data
from src.features import add_features
from src.model import train_model
from src.predict import load_model, predict_next_day
import pandas as pd

def main():
    print("Fetching data...")
    df = fetch_data()

    print("Generating features...")
    df = add_features(df)

    print("Training model...")
    train_model(df)

    print("Loading model and making prediction...")
    model = load_model()
    predicted_price = predict_next_day(df, model)
    print(f"Predicted closing price for next day: {predicted_price:.2f}")

if __name__ == "__main__":
    main()
