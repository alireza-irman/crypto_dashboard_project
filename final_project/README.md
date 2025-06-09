# Bitcoin Price Analyzer (7-Day Tracker)

This project is a **complete data analysis pipeline** built to fetch, process, and visualize Bitcoin prices over the last 7 days using real-time data from the CoinGecko API. It is designed as a practical learning project in Python, focusing on essential data analysis skills useful for AI, machine learning, and data-driven decision-making.

---

## ✨ Project Goals
- Strengthen skills in **Python programming**, **data collection**, and **data visualization**
- Demonstrate ability to structure code into modular components (`main.py` and `utils.py`)
- Provide a base for future financial analysis tools (e.g., price prediction, anomaly detection, etc.)

---

## 🌐 Features
- ✅ Fetches real-time Bitcoin price data (past 7 days)
- ✅ Converts JSON data into clean CSV format
- ✅ Generates a clear line chart and saves it as an image
- ✅ Clean, modular, and beginner-friendly Python code

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `main.py` | Entry point: coordinates the full pipeline from data fetching to visualization |
| `utils.py` | Helper functions: fetching API data, saving CSV, and plotting chart |
| `btc_prices.csv` | Output: historical price data in structured CSV format |
| `btc_price_chart.png` | Output: line chart image of Bitcoin price changes |
| `requirements.txt` | List of all Python dependencies |

---

## 📖 How to Use

### → 1. Install the required libraries:
```bash
pip install -r requirements.txt
```

### → 2. Run the project:
```bash
python main.py
```

This will generate both the CSV and the chart in the working directory.

---

## 🌟 Future Improvements
- [ ] Add date/time formatting options (local time zone support)
- [ ] Add interactive visualizations (e.g., Plotly or Dash)
- [ ] Extend to multi-coin tracking (ETH, ADA, etc.)
- [ ] Export chart to PDF or upload to cloud drive

---

## ✍️ Author

**Created by: Alireza Ahmadi**  
Specialist in AI, Data Analytics, and Educational Technology  
Inspired by real-world challenges and books on Python data analysis.

---

Feel free to fork, modify, or expand this project in your own data science journey.

> "Learning by building: every line of code brings us closer to real-world impact."
