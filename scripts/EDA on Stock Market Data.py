'''Stock Market Data Analysis & Visualization
Author: Priyanka Goswami
Date: October 2025

Description: 
This project performs comprehensive Exploratory Data Analysis (EDA) and visualization on stock market data using 
Yahoo Finance API (`yfinance`).
It compares multiple tech stocks (AAPL, MSFT, GOOGL) across 2024, analyzes correlations, and generates high-quality visualizations:
    • Line trends over time
    • Pairwise stock relationships
    • Candlestick charts for Apple (AAPL)
    • Correlation heatmap
    • Moving Averages for trend insight

Tools/Dependencies:
    1. Pandas
    2. Matplotlib
    3. Seaborn
    4. yfinance
    5. mplfinance'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import mplfinance as mpf
import os
os.makedirs("plots", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

sns.set_theme(style="whitegrid", context="talk", palette="Set3")

def fetch_data(tickers, start, end):
    try:
        data = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
        data.dropna(inplace=True)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[1] if isinstance(col, tuple) else col for col in data.columns]
        print(f"Successfully fetched data for: {', '.join(tickers)}")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    
#  Plot closing prices of all selected stocks.

def plot_line_chart(data):
    plt.figure(figsize=(12, 6))
    for stock in data.columns:
        plt.plot(data.index, data[stock], label=stock, linewidth=2.2, alpha=0.8)
    plt.title("Stock Prices Over Time (2024)", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend(title="Stock", loc="upper left")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join("plots/stock_trends.jpg"), dpi=300) 
    plt.show()

 # Plot pairwise relationships between different stocks.

def plot_pairplot(data):
    sns.pairplot(data)
    plt.suptitle("Stock Relationship Analysis", y=1.02, fontsize=16)
    plt.savefig(os.path.join("plots/pairwise_relationship_between_stocks.jpg"), dpi=300) 
    plt.show()

# Plot correlation heatmap between stocks.

def plot_correlation_heatmap(data):
    plt.figure(figsize=(6, 5))
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
    plt.title("Correlation Heatmap Between Stocks")
    plt.tight_layout()
    plt.savefig(os.path.join("plots/correlation_heatmap_between_stocks.jpg"), dpi=300) 
    plt.show()

# Plot moving averages for a single stock.

def plot_moving_averages(stock_symbol, start, end):
    df = yf.download(stock_symbol, start=start, end=end, auto_adjust=True)
    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price", linewidth=2)
    plt.plot(df.index, df["MA20"], label="20-Day MA", linestyle="--")
    plt.plot(df.index, df["MA50"], label="50-Day MA", linestyle="--")
    plt.title(f"{stock_symbol} Moving Averages (2024)", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig(os.path.join("plots/AAPL_moving_average.jpg"), dpi=300) 
    plt.tight_layout()
    plt.show()

# Plot candlestick chart for a stock.

def plot_candlestick(stock_symbol, start, end):
    df = yf.download(stock_symbol, start=start, end=end, auto_adjust=True)
    df.dropna(inplace=True)
    required_cols = ["Open", "High", "Low", "Close", "Volume"]
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]
    if not all(col in df.columns for col in required_cols):
        print(f"Error: Missing columns. Available columns: {df.columns.tolist()}")
        return
    df = df[required_cols].copy()
    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(inplace=True)
    mpf.plot(
        df.tail(60),
        type="candle",
        title=f"{stock_symbol} Candlestick Chart - Last 60 Days",
        style="charles",
        volume=True,
        mav=(10, 20),
        figsize=(12, 6),
    )
    plt.savefig(os.path.join("plots/AAPL_Candlestick.jpg"), dpi=300)
    plt.tight_layout()
  

if __name__ == "__main__":
    STOCKS = ["AAPL", "MSFT", "GOOGL"]
    START_DATE = "2024-01-01"
    END_DATE = "2025-01-01"
    stock_data = fetch_data(STOCKS, START_DATE, END_DATE)
    if not stock_data.empty:
        plot_line_chart(stock_data)
        plot_pairplot(stock_data)
        plot_correlation_heatmap(stock_data)
        plot_moving_averages("AAPL", START_DATE, END_DATE)
        plot_candlestick("AAPL", START_DATE, END_DATE)

# Summary Statistics

data = pd.DataFrame(stock_data)
data.describe().to_csv("outputs/stock_summary.csv")

print("EDA Completed Successfully! \nAll visualizations saved as JPG files. \nSummary table saved to 'outputs/stock_summary.csv'")