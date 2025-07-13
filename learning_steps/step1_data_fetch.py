"""
step1_data_fetch.py

This script fetches daily Bitcoin price data for the last 7 days
from the CoinGecko public API and stores it in a local JSON file
for later use in data analysis and visualization steps.

Part of the Crypto Dashboard Project by Alireza Irman.
"""

import requests
import json

def fetch_bitcoin_market_data():
    """
    Fetch 7-day Bitcoin price data (daily intervals) from CoinGecko API.

    Returns:
        dict: A dictionary containing keys such as 'prices', 'market_caps', and 'total_volumes'.
    Raises:
        Exception: If the API call fails or response structure is invalid.
    """
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': '7',
        'interval': 'daily'
    }

    try:
        # Send GET request to CoinGecko API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        data = response.json()

        # Check if expected key exists
        if "prices" not in data:
            raise ValueError("Missing 'prices' key in API response")

        return data
