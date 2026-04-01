'''Exploratory Data Analysis (EDA) on the Iris Dataset
Author: Priyanka Goswami
Date: october 2025

Description:
This project performs data exploration and visualization on the Iris dataset. It analyzes Iris's feature distributions, 
relationship between features, distribution of petal lengths acrosss pecies. 

Tools/Dependencies:
    1. Pandas: Data handling
    2. Matplotlib: Basic plotting
    3. Seaborn: Advanced statistical visualization'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
iris = load_iris()
df = pd.DataFrame(
    data=iris.data, 
    columns=iris.feature_names
)
df['species'] = [iris.target_names[i] for i in iris.target]
print("Dataset Loaded Successfully!\n")

# Plots to distribution of different features
# Using Histogram
df.hist(figsize=(12, 8), bins=15, color='teal', edgecolor='black')
plt.suptitle("Feature Distribution - Iris Dataset", fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig("plots/iris_histograms.png", dpi=300)
plt.show()
# Using Boxplots
plt.figure(figsize=(12, 6))
df_melted = df.melt(id_vars="species", var_name="Features", value_name="Values")
sns.boxplot(x="Features", y="Values", data=df_melted, hue="species", dodge=True, palette = 'inferno')
plt.title("Box Plot of Iris Features by Species", fontsize=18, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/iris_boxplots.png", dpi=300)
plt.show()

# Pair Plot visualizing relationships between features.

sns.pairplot(df, hue="species", diag_kind="kde", height=2.5, palette = 'magma')
plt.suptitle("Pairwise Feature Relationships in Iris Dataset", fontsize=18, fontweight='bold', y=1.02)
plt.savefig("plots/iris_pairplot.png", dpi=300)
plt.show()

# Violin Plot showing distribution of petal lengths across species.

plt.figure(figsize=(8, 6))
sns.violinplot(x="species", y="petal length (cm)", data=df, inner="quart", linewidth=1.2, palette = 'viridis',hue="species",legend=False)
plt.title("Distribution of Petal Length Across Species", fontsize=18, fontweight='bold')
plt.xlabel("Species", fontsize=14)
plt.ylabel("Petal Length (cm)", fontsize=14)
plt.tight_layout()
plt.savefig("plots/iris_violinplot.png", dpi=300)
plt.show()

# Summary Statistics

print("\nSummary Statistics (Overall):\n")
print(df.describe().T) 
df.describe().T.to_csv("outputs/iris_summary.csv")
print("EDA Completed Successfully! \nAll visualizations saved as PNG files. \nSummary table saved to 'outputs/iris_summary.csv'")