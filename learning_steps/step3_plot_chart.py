"""
step3_plot_chart.py

This script reads cleaned Bitcoin price data from 'btc_prices.csv' and plots
a line chart showing the price trend over the last 7 days using matplotlib.

Part of the Crypto Dashboard Project by Alireza Irman.
"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_csv(file_path):
    """
    Reads a CSV file with 'Date' and 'Price (USD)' columns.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        tuple: Two lists containing datetime objects (dates) and float prices.
    """
    dates = []
    prices = []

    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dates.append(datetime.strptime(row["Date"], "%Y-%m-%d"))
                prices.append(float(row["Price (USD)"]))
        return dates, prices
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return [], []
    except Exception as e:
        print("❌ Failed to read or parse CSV:", e)
        return [], []

def plot_chart(dates, prices, save_path="btc_price_chart.png"):
    """
    Plots a line chart of Bitcoin prices over time and saves it as PNG.

    Args:
        dates (list): List of datetime objects.
        prices (list): List of float price values.
        save_path (str): File path to save the output image.
    """
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(dates, prices, marker='o', linestyle='-', color='blue', label='Bitcoin Price')
        plt.title('Bitcoin Price in Last 7 Days')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to file
        plt.savefig(save_path)
        print(f"✅ Chart saved to {save_path}")

        # Show the plot
        plt.show()

    except Exception as e:
        print("❌ Failed to generate chart:", e)

if __name__ == "__main__":
    csv_path = "btc_prices.csv"
    dates, prices = read_csv(csv_path)
    if dates and prices:
        plot_chart(dates, prices)
