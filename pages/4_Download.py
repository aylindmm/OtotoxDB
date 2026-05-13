import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Download")
st.title("Data Download")

#st.cache_data.clear()
# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/articles.tsv", sep="\t")
    return df


df = load_data()

# Convert dataframe to CSV
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='articles.csv',
    mime='text/csv',
)

st.write(
    """
    The file contains the following columns:
"""
)