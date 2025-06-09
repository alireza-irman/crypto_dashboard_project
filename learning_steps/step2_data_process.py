import json
import csv
from datetime import datetime

def process_data():
    with open("btc_data.json", "r") as f:
        data = json.load(f)

    prices = data['prices']

    with open("btc_prices.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Price (USD)"])
        
        for entry in prices:
            timestamp = entry[0] / 1000
            date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
            price = round(entry[1], 2)
            writer.writerow([date, price])
    
    print("✅ Data saved to btc_prices.csv")

if __name__ == "__main__":
    process_data()
