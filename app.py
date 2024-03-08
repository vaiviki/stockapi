# app.py
import datetime

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from stockapi import train, model_train
import uvicorn

app = FastAPI(docs_url="/swagger", redoc_url="/redoc")

class StockModel(BaseModel):
    open: float
    high: float
    low: float
    close: float
    shares_traded: int
    volume: float
    traded_date: str




@app.post("/predict/")
async def predict(data: StockModel):
    # Convert the string to a datetime object
    date_object = datetime.strptime(StockModel.traded_date, "%Y-%m-%d")

    # Get the weekday (Monday is 0 and Sunday is 6)
    weekday_number = date_object.weekday()
    pred_params = {
        'Open': [StockModel.open],
        'High': [StockModel.high],
        'Low': [StockModel.low],
        'Close': [StockModel.close],
        'Shares Traded': [StockModel.shares_traded],
        'Turnover': [StockModel.volume],
        'Weekday': [3]}

    return {"prediction": train.getPredictions(pred_params)}

if __name__== "__main__":
   uvicorn.run(app, host="127.0.0.1", port=8080)