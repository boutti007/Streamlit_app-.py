import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load data
df = pd.read_csv('data/metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Interactive year range slider
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications by year
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title('Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
st.pyplot(fig)

# Show sample data
st.write("Sample Data", df_filtered.head())