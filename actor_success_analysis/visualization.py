import streamlit as st
import pandas as pd
import plotly.express as px

# Load the actor success data
actor_success = pd.read_csv('actor_success.csv')  # Save your actor success data if not already

# Streamlit app setup
st.title('Actor Success Analysis')
st.write('Explore which actors appear in the most movies and who delivers the highest-rated performances.')

# Top 10 Actors by Movie Count
st.subheader('Top 10 Actors by Movie Count')
top_actors_count = actor_success.sort_values(by='Movie_Count', ascending=False).head(10)
fig_count = px.bar(
    top_actors_count, 
    x='Actor', y='Movie_Count', 
    title='Top 10 Actors by Movie Count',
    labels={'Movie_Count': 'Number of Movies'},
    text='Movie_Count'
)
st.plotly_chart(fig_count, use_container_width=True)

# Top 10 Actors by Average IMDb Rating
st.subheader('Top 10 Actors by Average IMDb Rating')
top_actors_rating = actor_success.sort_values(by='Avg_IMDb_Rating', ascending=False).head(10)
fig_rating = px.bar(
    top_actors_rating, 
    x='Actor', y='Avg_IMDb_Rating', 
    title='Top 10 Actors by Average IMDb Rating',
    labels={'Avg_IMDb_Rating': 'Average IMDb Rating'},
    text='Avg_IMDb_Rating'
)
st.plotly_chart(fig_rating, use_container_width=True)