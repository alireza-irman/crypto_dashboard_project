import requests
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


def fetch_btc_data():
    """
    Fetches the last 7 days of Bitcoin price data from the CoinGecko API.

    Returns:
        dict: JSON data containing BTC price history.
    """
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "7",
        "interval": "hourly"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")
    return response.json()


def save_json_to_csv(data, file_path):
    """
    Converts CoinGecko JSON data to a CSV file.

    Args:
        data (dict): JSON data containing BTC prices.
        file_path (str or Path): Output CSV file path.
    """
    prices = data["prices"]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Date", "Price (USD)"])
        for timestamp, price in prices:
            date_str = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp, date_str, price])


def read_csv(file_path):
    """
    Reads the saved CSV file and returns separate lists for dates and prices.

    Args:
        file_path (str or Path): Path to the CSV file.

    Returns:
        list[str]: List of dates.
        list[float]: List of prices.
    """
    df = pd.read_csv(file_path)
    return df["Date"].tolist(), df["Price (USD)"].tolist()


def plot_and_save(dates, prices, output_path):
    """
    Plots Bitcoin prices and saves the figure as a PNG file.

    Args:
        dates (list): List of datetime strings.
        prices (list): List of BTC prices.
        output_path (str or Path): Output image file path.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, marker='o', linestyle='-', color='green')
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Bitcoin Price Over Last 7 Days")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
