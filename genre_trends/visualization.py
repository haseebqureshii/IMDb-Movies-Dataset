import streamlit as st
import pandas as pd
import plotly.express as px

# Load the genre trends data
genre_trends = pd.read_csv('genre_trends.csv')

# Create an interactive line chart with Plotly
fig = px.line(genre_trends, x='Released_Year', y='Count', color='Genre', 
              title='Genre Trends Over Time (Interactive)')

# Streamlit app setup
st.title('Film Genre Trends Over Time')
st.text('(Top 1000 Movies by IMDB Ratings)')
st.write('Explore how the popularity of different genres has evolved over the years.')

# Display the plot using Streamlit
st.plotly_chart(fig, use_container_width=True)