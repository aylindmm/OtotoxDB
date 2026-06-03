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
    label="Download compound data",
    data=csv,
    file_name='compounds.csv',
    mime='text/csv',
)


@st.cache_data
def load_data():
    df = pd.read_csv("data/targets.tsv", sep="\t")
    return df


df2 = load_data()

# Convert dataframe to CSV
csv2 = df2.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download target data",
    data=csv2,
    file_name='targets.csv',
    mime='text/csv',
)


@st.cache_data
def load_data():
    df = pd.read_csv("data/sources.tsv", sep="\t")
    return df


df3 = load_data()

# Convert dataframe to CSV
csv3 = df3.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download aticle data",
    data=csv3,
    file_name='articles.csv',
    mime='text/csv',
)

st.divider()

st.write("To install a local version of this app, visit this [GitHub repository](https://github.com/aylindmm/Ototoxic_DB)")