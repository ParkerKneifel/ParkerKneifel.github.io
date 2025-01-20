import yfinance as yf
import json

# Fetch SPY data for 2024
ticker = 'SPY'
data = yf.download(ticker, start="2024-01-01", end="2025-01-01", interval='1mo')

# Prepare the data
monthly_data = {
    "labels": [str(date)[:10] for date in data.index],
    "values": data['Close'].tolist()
}

# Save the data to a JSON file
with open('spy_2024_data.json', 'w') as f:
    json.dump(monthly_data, f)
