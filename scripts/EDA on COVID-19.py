'''Data Analysis & Visualization of COVID-19 Trends
Author: Priyanka Goswami
Date: October 2025

Description: 
This project performs comprehensive Exploratory Data Analysis (EDA) and visualization on COVID-19 dataset.
It Analyze COVID-19 data, such as infection rates, recoveries, and deaths across different countries and generates high-quaqlity visualizations.
analyzes correlations, and generates high-quality visualizations:
    • Line plots showing the trends over time
    • Correlation Heatmap between different metrics like cases, deaths, and recoveries
    • Compare data between multiplie countries using bar charts and box plots.
    • Normalize comparisons
    • Summarize statistics

Tools/Dependecies:
    1. Pandas 
    2. Matplotlib
    3. Seaborn'''

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.makedirs("plots", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
try:
    data = pd.read_csv("covid_19_data.csv")
    print("Dataset Loaded Successfully!\n")
except FileNotFoundError:
    print("The file 'covid_19_data.csv' was not found. Please place it in the same directory.")

data['Date'] = pd.to_datetime(data['Date'],errors='coerce')
data.fillna({'Cases':0, 'Deaths':0, 'Recovered':0}, inplace=True)
data['Active'] = data['Cases'] - (data['Deaths'] + data['Recovered'])
data['Fatality_Rate'] = (data['Deaths'] / data['Cases']) * 100
data['Recovery_Rate'] = (data['Recovered'] / data['Cases']) * 100

# Plotting trends over time for a specific country

country = 'India'
country_data = data[data['Country'] == country]
plt.figure(figsize=(14,7))
plt.plot(country_data['Date'], country_data['Cases'], label='Cases', color="#61fde0", linewidth=2, marker='o', markersize=5)
plt.plot(country_data['Date'], country_data['Deaths'], label='Deaths', color="#ffe438", linewidth=2, marker='x', markersize=5)
plt.plot(country_data['Date'], country_data['Recovered'], label='Recovered', color="#00ff00", linewidth=2, marker='s', markersize=5)
plt.plot(country_data['Date'], country_data['Active'], label='Active', color="#a20909", linewidth=2, linestyle='--', marker='d', markersize=4)
plt.title(f"COVID-19 Trends in {country}", fontsize=20, weight='bold')
plt.xlabel("Date", fontsize=12)
plt.ylabel("Number of Cases", fontsize=12)
plt.legend(title='Metrics', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("plots/covid_trends_india.png"), dpi=300) 
plt.show()

# Correlation Heatmap Between Metrics

metrics = data[['Cases', 'Deaths', 'Recovered', 'Active', 'Fatality_Rate', 'Recovery_Rate']]
plt.figure(figsize=(8,6))
sns.heatmap(metrics.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Between COVID-19 Metrics")
plt.savefig("plots/correlation_heatmap.png", dpi=300)
plt.show()

# Comparing data between countries
# Using Barplots
countries = ['India', 'United States', 'Brazil', 'Italy', 'China']
subset = data[data['Country'].isin(countries)]
latest = subset.groupby('Country')[['Cases', 'Deaths', 'Recovered']].max().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(x='Country', y='Cases', data=latest.sort_values('Cases', ascending=False),color = "red")
plt.title("Total Confirmed Cases by Country",fontsize = 16)
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Using Boxplots
plt.figure(figsize=(10,6))
sns.boxplot(x='Country', y='Deaths', data=subset, color = 'cyan')
plt.title("Distribution of Deaths Across Countries")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("plots/cases_by_country.png"), dpi=300)
plt.show()

# Normalized Comparison (Per 100K Cases)

latest['Death_to_Case_%'] = (latest['Deaths'] / latest['Cases']) * 100
latest['Recovery_to_Case_%'] = (latest['Recovered'] / latest['Cases']) * 100
plt.figure(figsize=(8,6))
sns.barplot(x='Country', y='Death_to_Case_%', data=latest, label='Fatality %', color='blue')
sns.barplot(x='Country', y='Recovery_to_Case_%', data=latest, alpha=0.7, label='Recovery %', color='yellow')
plt.title("Death vs Recovery Rate by Country (%)")
plt.ylabel("Percentage (%)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("plots/death_vs_recovery.png"), dpi=300)
plt.show()

# Summary Statistics

summary = latest[['Country', 'Cases', 'Deaths', 'Recovered', 'Death_to_Case_%', 'Recovery_to_Case_%']]
print("\nFinal Summary Table:\n")
print(summary.round(2))

# Save summary to CSV
summary.to_csv("outputs/covid_summary.csv", index=False)
print("EDA Completed Successfully! \nAll visualizations saved as PNG files. \nSummary table saved to 'outputs/covid_summary.csv'")