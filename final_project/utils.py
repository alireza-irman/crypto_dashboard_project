
import requests
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def fetch_btc_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "7",
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    return response.json()

def save_json_to_csv(json_data, csv_filename):
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Price (USD)"])
        for item in json_data["prices"]:
            timestamp, price = item
            date = datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
            writer.writerow([date, round(price, 2)])

def read_csv(file_path):
    dates = []
    prices = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dates.append(datetime.strptime(row["Date"], "%Y-%m-%d"))
            prices.append(float(row["Price (USD)"]))
    return dates, prices

def plot_and_save(dates, prices, filename="btc_price_chart.png"):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='green', label='Bitcoin Price')
    plt.title('Bitcoin Price in Last 7 Days')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
