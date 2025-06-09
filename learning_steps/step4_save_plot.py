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

def plot_and_save(dates, prices, filename="btc_price_chart.png"):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker='o', linestyle='-', color='green', label='Bitcoin Price')
    plt.title('Bitcoin Price in Last 7 Days')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)  # ذخیره به عنوان فایل تصویر
    print(f"✅ نمودار در فایل {filename} ذخیره شد.")

if __name__ == "__main__":
    dates, prices = read_csv("btc_prices.csv")
    plot_and_save(dates, prices)
