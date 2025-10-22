import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

df = pd.read_csv('netflix_titles.csv')

print("Shape of dataset:", df.shape)
print("Columns:", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())

df.drop_duplicates(inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['director'].fillna('No Director', inplace=True)
df['cast'].fillna('No Cast', inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

def plot_content_type(df):
    sns.countplot(data=df, x='type', palette='Set2')
    plt.title('Distribution of Content Type')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_yearly_additions(df):
    sns.histplot(data=df, x='year_added', hue='type', multiple='stack', bins=20)
    plt.title('Content Added Over the Years')
    plt.xlabel('Year Added')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_top_countries(df):
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='magma')
    plt.title('Top 10 Countries by Content Count')
    plt.xlabel('Number of Titles')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.show()

def plot_top_genres(df):
    genre_series = df['listed_in'].dropna().apply(lambda x: x.split(', '))
    genre_counts = Counter([genre for sublist in genre_series for genre in sublist])
    top_genres = genre_counts.most_common(10)
    genres, counts = zip(*top_genres)
    sns.barplot(x=list(counts), y=list(genres), palette='coolwarm')
    plt.title('Top 10 Genres on Netflix')
    plt.xlabel('Number of Titles')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.show()

def plot_rating_distribution(df):
    sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index, palette='pastel')
    plt.title('Content Rating Distribution')
    plt.xlabel('Count')
    plt.ylabel('Rating')
    plt.tight_layout()
    plt.show()

def plot_duration_distribution(df):
    movie_df = df[df['type'] == 'Movie']
    movie_df['duration_minutes'] = movie_df['duration'].str.extract('(\d+)').astype(float)
    sns.histplot(movie_df['duration_minutes'], bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Movie Durations')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

def plot_tv_show_seasons(df):
    tv_df = df[df['type'] == 'TV Show']
    tv_df['seasons'] = tv_df['duration'].str.extract('(\d+)').astype(int)
    sns.countplot(x=tv_df['seasons'], palette='viridis')
    plt.title('Number of Seasons in TV Shows')
    plt.xlabel('Seasons')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_director_frequency(df):
    top_directors = df['director'].value_counts().head(10)
    sns.barplot(x=top_directors.values, y=top_directors.index, palette='cubehelix')
    plt.title('Top 10 Directors by Number of Titles')
    plt.xlabel('Number of Titles')
    plt.ylabel('Director')
    plt.tight_layout()
    plt.show()

def plot_cast_frequency(df):
    cast_series = df['cast'].dropna().apply(lambda x: x.split(', '))
    cast_counts = Counter([actor.strip() for sublist in cast_series for actor in sublist])
    top_cast = cast_counts.most_common(10)
    actors, counts = zip(*top_cast)
    sns.barplot(x=list(counts), y=list(actors), palette='flare')
    plt.title('Top 10 Most Featured Actors')
    plt.xlabel('Number of Titles')
    plt.ylabel('Actor')
    plt.tight_layout()
    plt.show()

plot_content_type(df)
plot_yearly_additions(df)
plot_top_countries(df)
plot_top_genres(df)
plot_rating_distribution(df)
plot_duration_distribution(df)
plot_tv_show_seasons(df)
plot_director_frequency(df)
plot_cast_frequency(df)