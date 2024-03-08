import requests

# Define input data
input_data = {
    'open': 22505.30,
    'high': 22525.65,
    'low': 22430.00,
    'close': 22493.55,
    'shares_traded': 379865142,
    'volume': 33558.65,
    'traded_date':'2024-03-07'}

# Send POST request to FastAPI endpoint
response = requests.post("http://127.0.0.1:8080/predict/", json=input_data)

# Print prediction
print("######",response.text)

