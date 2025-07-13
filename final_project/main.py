"""
main.py

This script serves as the main entry point of the Bitcoin Price Analyzer project.
It automates the full workflow:
1. Fetch BTC price data from CoinGecko API
2. Convert JSON to CSV format
3. Read and process the CSV
4. Plot and save the chart as PNG

Author: Alireza Irman
"""

from utils import fetch_btc_data, save_json_to_csv, read_csv, plot_and_save

def main():
    print("📡 Fetching BTC price data from API...")
    try:
        data = fetch_btc_data()
    except Exception as e:
        print(f"❌ Failed to fetch data: {e}")
        return

    print("💾 Saving JSON data to CSV...")
    try:
        save_json_to_csv(data, "btc_prices.csv")
    except Exception as e:
        print(f"❌ Failed to convert JSON to CSV: {e}")
        return

    print("📊 Reading CSV and generating chart...")
    try:
        dates, prices = read_csv("btc_prices.csv")
        plot_and_save(dates, prices)
    except Exception as e:
        print(f"❌ Failed to read CSV or plot chart: {e}")
        return

    print("✅ All done! Chart saved as btc_price_chart.png")

if __name__ == "__main__":
    main()
