"""
step4_save_plot.py

This script reads cleaned Bitcoin price data from 'btc_prices.csv',
plots a line chart using matplotlib, and saves the chart as a PNG image.

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

def plot_and_save(dates, prices, filename="btc_price_chart.png"):
    """
    Plots a Bitcoin price chart and saves it to a PNG file.

    Args:
        dates (list): List of datetime objects (X-axis).
        prices (list): List of float values (Y-axis).
        filename (str): Path to save the chart image.
    """
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(dates, prices, marker='o', linestyle='-', color='green', label='Bitcoin Price')
        plt.title('Bitcoin Price in Last 7 Days')
        plt.xlabel('Date')
        plt.yla
