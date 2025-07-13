# 🧠 Learning Steps: Bitcoin Price Analyzer

This folder contains the educational and incremental development steps used to build the final version of the Bitcoin Price Analyzer project. Each step introduces a new concept such as API usage, JSON processing, CSV export, and chart visualization using Python.

> 📁 These files are designed for **learning purposes** and follow a modular structure to help beginners understand how each part contributes to the final product.

---

## ✅ Step-by-Step Overview

### 🟩 Step 1 - Fetch BTC Price from API  
**File**: `step1_data_fetch.py`  
**Goal**: Connect to the [CoinGecko API](https://www.coingecko.com/en/api), retrieve 7-day historical price data for Bitcoin, and save the raw JSON to `btc_data.json`.

---

### 🟨 Step 2 - Process JSON to CSV  
**File**: `step2_data_process.py`  
**Goal**: Convert the raw JSON into a clean CSV file named `btc_prices.csv` with readable dates and formatted prices.

---

### 🟦 Step 3 - Plot Line Chart  
**File**: `step3_plot_chart.py`  
**Goal**: Visualize the Bitcoin prices using `matplotlib`. This step displays a line chart of prices over time.

---

### 🟥 Step 4 - Save Chart as PNG  
**File**: `step4_save_plot.py`  
**Goal**: Same as Step 3, but also **saves the chart as an image** file `btc_price_chart.png` for use in reports, GitHub repos, or LinkedIn portfolios.

---

## 🧪 How to Run

You can execute each step individually using the following commands:

```bash
python step1_data_fetch.py
python step2_data_process.py
python step3_plot_chart.py
python step4_save_plot.py
```

Make sure your working directory contains all the required files and dependencies.

---

## 🧰 Dependencies

Install required Python packages:

```bash
pip install requests matplotlib
```

Also uses:
- `csv`, `json`, `datetime` (built-in)

---

## 📸 Sample Output

- **btc_data.json** → Raw API data
- **btc_prices.csv** → `Date, Price (USD)`
- **btc_price_chart.png** → Line chart image (saved to disk)

---

## 🚧 Coming Soon

- Statistical analysis (mean, median, volatility)
- Interactive dashboard
- Final project packaging and deployment
