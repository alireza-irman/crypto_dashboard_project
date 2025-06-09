import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_csv(file_path):
    dates = []
    prices = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dates.append(datetime.strptime(row["Date"], "%Y-%m-%d"))
            prices.append(float(row["Price (USD)"]))

    return dates, prices

def plot_chart(dates, prices):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='blue', label='Bitcoin Price')
    plt.title('Bitcoin Price in Last 7 Days')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    dates, prices = read_csv("btc_prices.csv")
    plot_chart(dates, prices)
