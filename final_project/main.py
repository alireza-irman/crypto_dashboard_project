
from utils import fetch_btc_data, save_json_to_csv, read_csv, plot_and_save

def main():
    print("Fetching data...")
    data = fetch_btc_data()

    print("Saving to CSV...")
    save_json_to_csv(data, "btc_prices.csv")

    print("Reading CSV and generating chart...")
    dates, prices = read_csv("btc_prices.csv")
    plot_and_save(dates, prices)

    print("✅ All done! Chart saved as btc_price_chart.png")

if __name__ == "__main__":
    main()
