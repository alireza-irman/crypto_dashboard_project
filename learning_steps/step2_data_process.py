"""
step2_data_process.py

This script reads raw Bitcoin price data from 'btc_data.json' and converts it
into a clean CSV file ('btc_prices.csv') with readable date and rounded price values.

Part of the Crypto Dashboard Project by Alireza Irman.
"""

import json
import csv
from datetime import datetime

def convert_json_to_csv(input_json_path="btc_data.json", output_csv_path="btc_prices.csv"):
    """
    Converts CoinGecko Bitcoin price JSON data to a clean CSV format.

    Args:
        input_json_path (str): Path to the input JSON file.
        output_csv_path (str): Path to save the processed CSV file.

    Raises:
        FileNotFoundError: If the input file is not found.
        KeyError: If 'prices' key is missing from the JSON structure.
    """
    try:
        # Read raw JSON data from file
        with open(input_json_path, "r") as f:
            data = json.load(f)

        # Extract the 'prices' list
        prices = data["prices"]

        # Write to CSV with formatted dates and rounded prices
        with open(output_csv_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Price (USD)"])

            for timestamp_ms, price in prices:
                # Convert Unix timestamp (ms) to readable date
                date = datetime.utcfromtimestamp(timestamp_ms / 1000).strftime('%Y-%m-%d')
                writer.writerow([date, round(price, 2)])

        print(f"✅ Data saved to {output_csv_path}")

    except FileNotFoundError:
        print(f"❌ File not found: {input_json_path}")
    except KeyError:
        print("❌ 'prices' key missing in JSON file.")
    except Exception as e:
        print("❌ Unexpected error:", e)

if __name__ == "__main__":
    convert_json_to_csv()
