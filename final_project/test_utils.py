"""
test_utils.py

Unit tests for utils.py functions in the Crypto Dashboard project.
Run using: pytest test_utils.py
"""

import pytest
from utils import fetch_btc_data, save_json_to_csv, read_csv

def test_fetch_btc_data_returns_dict():
    data = fetch_btc_data()
    assert isinstance(data, dict), "Expected the fetched data to be a dictionary"

def test_save_json_to_csv_creates_file(tmp_path):
    # Sample data
    sample_data = {
        "prices": [
            [1710015600000, 61000.35],
            [1710026400000, 61234.12]
        ]
    }
    test_file = tmp_path / "test_prices.csv"
    save_json_to_csv(sample_data, test_file)
    assert test_file.exists(), "CSV file should be created"

def test_read_csv_returns_lists(tmp_path):
    # Prepare test CSV
    content = "Date,Price\n2024-03-09,61000.35\n2024-03-09,61234.12\n"
    test_file = tmp_path / "sample.csv"
    test_file.write_text(content)

    dates, prices = read_csv(test_file)
    assert len(dates) == 2
    assert isinstance(prices[0], float)
