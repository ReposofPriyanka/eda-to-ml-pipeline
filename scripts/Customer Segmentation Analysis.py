'''Customer Segmentation Analysis & Visualization
Author: Priyanka Goswami
Date: October 2025

Description:
Segment customers based on purchasing behavior using data visualization and clustering.

Tools:
    1. Pandas for data handling
    2. Matplotlib for basic visualization
    3. Seaborn for advanced plots and clustering'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import os
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

os.makedirs("plots", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

sns.set(style="whitegrid", palette="pastel",context="paper")

try:
    data = pd.read_csv("customer_data.csv")
    print("Dataset Loaded Successfully!")
except FileNotFoundError:
    print("The file 'customer_data.csv' was not found. Please place it in the same directory.")
    exit()

# Age vs Spending Score
plt.figure(figsize=(8,6))
sns.scatterplot(data=data, x="Age", y="Spending_Score", hue="Annual_Income", palette="viridis", s=80)
plt.title("Customer Segmentation Based on Age, Income, and Spending Score", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.legend(title="Annual Income", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("plots/age_vs_spending_score.png", dpi=300)
plt.show()

# Correlation Analysis

plt.figure(figsize=(6,5))
corr = data[["Age", "Annual_Income", "Spending_Score"]].corr()
sns.heatmap(corr, annot=True, cmap="magma", linewidths=0.5)
plt.title("Correlation Between Customer Attributes")
plt.tight_layout()
plt.savefig("plots/customer_correlation_heatmap.png", dpi=300)
plt.show()

# Clustering Visualization

sns.clustermap(data[["Age", "Annual_Income", "Spending_Score"]], standard_scale=1, cmap="mako", figsize=(8,6))
plt.suptitle("Customer Clustermap", y=1.02)
plt.savefig("plots/customer_clustermap.png", dpi=300)
plt.show()

# K-Means Clustering 

X = data[["Age", "Annual_Income", "Spending_Score"]]
kmeans = KMeans(n_clusters=4, random_state=42)
data["Cluster"] = kmeans.fit_predict(X)
plt.figure(figsize=(8,6))
sns.scatterplot(data=data, x="Annual_Income", y="Spending_Score", hue="Cluster", palette="deep", s=80)
plt.title("K-Means Clustering of Customers")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.savefig("plots/customer_kmeans_clustering.png", dpi=300)
plt.show()

data.describe().to_csv("outputs/Customer_segmentation_summary.csv")
print("Customer Segmentation Analysis Completed Successfully!\nAll visualizations saved as PNG files. \nSummary table saved to 'outputs/customer_segmentation_summary.csv'.")