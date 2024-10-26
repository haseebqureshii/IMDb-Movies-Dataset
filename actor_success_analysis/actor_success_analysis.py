import pandas as pd

# Load the dataset
df = pd.read_csv('./dataset/imdb_top_1000.csv')

# Combine all actor columns (Star1, Star2, Star3, Star4) into a single column
actor_columns = ['Star1', 'Star2', 'Star3', 'Star4']
df['Actors'] = df[actor_columns].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)

# Split the combined actors column into individual rows (explode)
df_exploded = df.assign(Actor=df['Actors'].str.split(', ')).explode('Actor')

# Group by actor and calculate the number of movies and average IMDb rating
actor_success = df_exploded.groupby('Actor').agg(
    Movie_Count=('Series_Title', 'count'),
    Avg_IMDb_Rating=('IMDB_Rating', 'mean')
).reset_index()

actor_success.to_csv('actor_success.csv', index=False)