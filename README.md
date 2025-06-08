# 📈 Stock Price Prediction using Machine Learning

Welcome to my machine learning project where I explore how historical stock market data can be used to predict the next day's closing price of the **S&P 500 index**.

---

## 🧠 Problem Statement

Stock prices are inherently volatile, but within the chaos lie patterns.  
This project aims to use machine learning — specifically, a Random Forest Regressor — to predict the **next day’s closing price** based on historical trends.

---

## 🛠️ Tech Stack

- **Python 3.x**
- `yfinance` – to retrieve real-time and historical stock data
- `pandas`, `numpy` – for data preprocessing and manipulation
- `scikit-learn` – for building and evaluating the ML model
- `matplotlib` – for visualizations
- `joblib` – to save the trained model

---

## 📊 Dataset

The dataset was sourced using the `yfinance` API and contains over 10 years of daily historical data for the S&P 500 index.  
Key features used:
- Closing price
- 5-day and 10-day moving averages
- Volume

---

## 🔍 Model Used

We used a **Random Forest Regressor**, which is great for capturing non-linear patterns in time series data and works well with limited features.

### Why not linear regression?

Stock prices aren't linearly dependent on just one variable — Random Forest helps us dig deeper into complex interactions and capture more subtle trends.

---

## 🧪 Model Evaluation

- **Train/Test Split**: Standard 80/20 ratio
- **Evaluation Metric**: RMSE (Root Mean Squared Error)
- The model performs with reasonable accuracy and is capable of capturing short-term fluctuations effectively.

---

## 🤖 Prediction

Once trained, the model takes the latest available data and predicts the **next day's closing price**.  
Here’s a sample prediction output:
