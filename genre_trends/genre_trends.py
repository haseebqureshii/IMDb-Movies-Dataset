import pandas as pd

# Load the dataset
df = pd.read_csv('./dataset/imdb_top_1000.csv')

# Inspect the dataset to ensure the columns are correctly loaded
print(df.head())

# Check for missing values in the Released_Year or Genre columns
print(df[['Released_Year', 'Genre']].isna().sum())

# Drop rows with missing values in Released_Year or Genre
df = df.dropna(subset=['Released_Year', 'Genre'])

# Ensure Released_Year is an integer
df['Released_Year'] = df['Released_Year'].astype(int)

# Split genres if movies have multiple genres listed (e.g., "Action, Adventure")
df['Genre'] = df['Genre'].str.split(', ')

# Explode the Genre column so each genre has its own row
df_exploded = df.explode('Genre')

# Group by Released_Year and Genre, and count the number of movies for each genre per year
genre_trends = df_exploded.groupby(['Released_Year', 'Genre']).size().reset_index(name='Count')

# Save the processed data for visualization (optional)
genre_trends.to_csv('genre_trends.csv', index=False)