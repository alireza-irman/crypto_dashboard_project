
from utils import fetch_btc_data

def test_fetch_btc_data_returns_dict():
    data = fetch_btc_data()
    assert isinstance(data, dict), "The fetched data should be a dictionary"
