import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('../dataset/imdb_top_1000.csv')

# Clean the Gross column (e.g., "$123,456,789" -> 123456789)
df['Gross'] = df['Gross'].str.replace(',', '').astype(float)

# Explode the Genre column to handle multiple genres per movie
df['Genre'] = df['Genre'].str.split(', ')
df_exploded = df.explode('Genre')

# Group by Genre and calculate the average gross earnings
genre_gross = df_exploded.groupby('Genre').agg(
    Avg_Gross=('Gross', 'mean')
).reset_index()

# Format the Avg_Gross values to be more readable (e.g., 12.3M)
genre_gross['Avg_Gross'] = genre_gross['Avg_Gross'].apply(lambda x: f"${x:,.0f}")

# Streamlit App setup
st.title('Gross Earnings vs. Genre')
st.write('Explore which genres generate the highest average gross earnings.')

# Custom light color palette with 21 distinct colors
light_colors = [
    '#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6',
    '#ffffcc', '#fbc5c5', '#c5e0dc', '#f2b5c2', '#e6f7d8',
    '#d9d9f3', '#f9c2b2', '#f1f0f1', '#e7e1ef', '#b3e5b4',
    '#fee8c8', '#f2f3e0', '#cce5ff', '#d3e2f7', '#f9e5b2',
    '#d9d9d9'
]

# Create a bar chart to display average gross earnings by genre
fig = px.bar(
    genre_gross, x='Genre', y='Avg_Gross',
    title='Average Gross Earnings by Genre',
    labels={'Avg_Gross': 'Average Gross Earnings (USD)'},
    text='Avg_Gross',
    color='Genre',  # Assigns a different color to each genre
    color_discrete_sequence=light_colors  # Optional: Choose a color palette
)

# Display the chart using Streamlit
st.plotly_chart(fig, use_container_width=True)