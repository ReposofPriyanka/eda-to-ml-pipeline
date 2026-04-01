'''Exploratory Data Analysis (EDA) on movie ratings data
Author: Priyanka Goswami
Date: october 2025

Description:
This project performs comprehensive Exploratory Data Analysis (EDA) and visualization on movie ratings data. It analyze movie 
ratings data, such as average ratings, distribution of ratings by genre, and generates high-quality visualizations.
    • Bar plots showing the average ratings of movies over the years 
    • Swarm plot visualizes the distribution of ratings by genre
    • Boxplot compares ratings across different genres
    • Summarize statistics

Tools/Dependencies:
    1. Pandas
    2. Matplotlib
    3. Seaborn'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("plots", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

sns.set_theme(style="whitegrid", context="talk", palette="Set3")

Data = "rotten_tomatoes_movies.csv"
if not os.path.exists(Data):
    raise FileNotFoundError(f"Dataset not found at {Data}. Please place the file in this directory.")
else:
    movies = pd.read_csv(Data)
    print(f"Dataset Loaded Successfully with {movies.shape[0]} rows, {movies.shape[1]} columns\n")

movies.dropna(subset=["Genre", "Year", "Rating"], inplace=True)
movies["Year"] = movies["Year"].astype(int)
movies["Rating"] = movies["Rating"].astype(float)

# Average Rating Over the Years

avg_rating = movies.groupby("Year")["Rating"].mean().reset_index()
plt.figure()
plt.plot(avg_rating["Year"], avg_rating["Rating"], color="teal", marker="o")
plt.title("Average Movie Ratings Over the Years", fontsize=14, weight="bold")
plt.xlabel("Year")
plt.ylabel("Average Rating")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join("plots/avg_ratings_over_years.png"),dpi = 300)
plt.show()

# Swarm Plot: Ratings by Genre
plt.figure(figsize=(10, 6))
sns.swarmplot(data=movies, x="Genre", y="Rating", size=3, edgecolor="black", linewidth=0.3,alpha=0.7, palette="magma", hue="Genre", legend=False)
plt.title("Distribution of Ratings by Genre", fontsize=14, weight="bold")
plt.xlabel("Genre")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("plots/ratings_by_genre_swarm_plot.png"),dpi = 300)
plt.show()

# Boxplot: Ratings Comparison Across Genres

plt.figure()
sns.boxplot(data=movies, x="Genre", y="Rating", palette="pastel", fliersize=3, linewidth=1, width=0.6, hue="Genre", legend=False, dodge=False)
plt.title("Boxplot of Ratings Across Genres", fontsize=14, weight="bold")
plt.xlabel("Genre")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("plots/ratings_by_genre_boxplot.png"),dpi = 300)
plt.show()

# Summary Statistics

movies.describe().round(2).to_csv(os.path.join("outputs/movie_ratings_summary.csv"))
print("EDA Completed Successfully! \nAll visualizations saved as JPG files. \nSummary table saved to 'outputs/movie_ratings_summary.csv'")