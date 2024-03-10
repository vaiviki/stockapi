# app.py
from datetime import datetime
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from stockapi import train, model_train
import uvicorn
from fastapi import APIRouter, FastAPI, Request

from config import settings

app = FastAPI(docs_url="/swagger", redoc_url="/redoc")

root_router = APIRouter()
class StockModel(BaseModel):
    open: float
    high: float
    low: float
    close: float
    shares_traded: int
    volume: float
    traded_date: str
    
    
@root_router.get("/")
def index(request: Request) -> Any:
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )

    return HTMLResponse(content=body)






@app.post("/predict/")
async def predict(data: StockModel):
    # Convert the string to a datetime object
    date_object = datetime.strptime(data.traded_date, "%Y-%m-%d")

    # Get the weekday (Monday is 0 and Sunday is 6)
    weekday_number = date_object.weekday()
    pred_params = {
        'Open': [data.open],
        'High': [data.high],
        'Low': [data.low],
        'Close': [data.close],
        'Shares Traded': [data.shares_traded],
        'Turnover': [data.volume],
        'Weekday': [3]}
    print(pred_params)

    return {"prediction": train.getPredictions(pred_params)}

if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
