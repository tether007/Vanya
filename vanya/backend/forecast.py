import pandas as pd
from prophet import Prophet

def forecast_wildlife():
    # mock dataset
    data = pd.DataFrame({
        "ds": pd.date_range("2023-01-01", periods=12, freq="M"),
        "y": [50,52,48,47,46,45,44,42,41,40,39,38]  # elephant counts
    })
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=6, freq="M")
    forecast = model.predict(future)
    return forecast[["ds","yhat"]].tail(6).to_dict(orient="records")
