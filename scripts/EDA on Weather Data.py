'''Exploratory Data Analysis (EDA) on weather data
Author: Priyanka Goswami
Date: october 2025

Description:
Description:
This project analyzes and visualizes weather data using Python.

Features:
- Load and preprocess weather data
- Plot temperature trends over time
- Explore relationship between temperature and humidity
- Visualize correlations between weather parameters

Dependencies:
    1. Pandas: Data handling
    2. Matplotlib: Basic plotting
    3. Seaborn: Advanced statistical visualization'''

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
def main():
    try:
        data = 'weather_data.csv'
        if not os.path.exists(data):
            print(f"Error: File '{data}' not found.")
            sys.exit(1)
        weather = pd.read_csv(data)
        weather['Date'] = pd.to_datetime(weather['Date'], errors='coerce')
        weather.dropna(subset=['Date', 'Temperature', 'Humidity', 'WindSpeed'], inplace=True)
        print("Data loaded successfully!\n")
        print("Dataset Summary:")
        print(weather.describe())
        
# Line plots showing temperature changes over time

        plt.figure(figsize=(10, 6))
        plt.plot(weather['Date'], weather['Temperature'], color='orange', linewidth=2)
        plt.title('Temperature Trend Over Time', fontsize=14)
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.savefig(os.path.join("plots/temparature_changes_overtime.jpg"), dpi=300) 
        plt.show()

# Scatter plots showing the relationship between temperature and humidity

        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='Temperature', y='Humidity', data=weather, color='royalblue', edgecolor='black', alpha=0.7)
        plt.title('Temperature vs Humidity', fontsize=14)
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Humidity (%)')
        plt.tight_layout()
        plt.savefig(os.path.join("plots/relationship_between_temparature_&_humidity.jpg"), dpi=300) 
        plt.show()

# Heatmap visualizing correlations among temperature, humidity, and wind speed

        plt.figure(figsize=(6, 5))
        correlation_matrix = weather[['Temperature', 'Humidity', 'WindSpeed']].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Correlation Between Weather Parameters', fontsize=14)
        plt.tight_layout()
        plt.savefig(os.path.join("plots/correlation_between_temparature_humidity_windspeed.jpg"), dpi=300) 
        plt.show()
        print("EDA Completed Successfully! \nAll visualizations saved as JPG files. \nSummary table saved to 'outputs/weather_summary.csv'")       
    except Exception as e:
        print(f"⚠️ An error occurred: {e}!")

if __name__ == "__main__":
    main()