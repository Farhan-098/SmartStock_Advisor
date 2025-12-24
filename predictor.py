import numpy as np
from sklearn.linear_model import LinearRegression

def predict(df):
    df["Days"] = np.arange(len(df))

    X = df[["Days"]].values
    y = df["Close"].values

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(df) + 1]])
    predicted_price = model.predict(next_day)[0]
    last_close = df["Close"].iloc[-1]

    change = ((predicted_price - last_close) / last_close) * 100

    if change > 1:
        decision, color = "✅ BUY", "green"
    elif change < -1:
        decision, color = "❌ SELL / NOT BUY", "red"
    else:
        decision, color = "🟡 HOLD", "orange"

    return round(change, 2), decision, color
