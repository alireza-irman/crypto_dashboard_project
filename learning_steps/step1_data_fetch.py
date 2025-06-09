# step1_data_fetch.py
import requests
import json

def fetch_price_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': '7',
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    bitcoin_data = fetch_price_data()
    with open("btc_data.json", "w") as f:
        json.dump(bitcoin_data, f, indent=2)
    print("Data saved to btc_data.json")
