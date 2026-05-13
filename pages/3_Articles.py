import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Articles")
st.title("Articles")
st.write(
    """
All articles found in PubMed and referenced in the database. You can filter by publication type and year.
"""
)
#st.cache_data.clear()
# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/sources.tsv", sep="\t")
    return df


df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
pub_types = st.multiselect(
    "Publication Types",
    df.PublicationTypes.unique(),
    df.PublicationTypes.unique()
)

# Show a slider widget with the years using `st.slider`.
years = st.slider("Years",1950, 2026, (1950, 2026))

df = df[["PMID", "Year", "Title", "PublicationTypes", "DOI"]]

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["PublicationTypes"].isin(pub_types)) & (df["Year"].between(years[0], years[1]))]
df_filtered = df_filtered.sort_values(by="Year", ascending=False)

# Convert the PMID column to string to link to PubMed.
df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  
df_filtered['DOI'] = df_filtered['DOI'].apply(lambda x: f"https://doi.org/{x}" if pd.notnull(x) else x)

# Convert dataframe to CSV
csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='articles.csv',
    mime='text/csv',
)

# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_filtered,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("Year"),
                   "PublicationTypes" : st.column_config.TextColumn("Publication Types"),
                   "PMID": st.column_config.LinkColumn("PMID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"), # click on PMID to go to PubMed
                   "DOI": st.column_config.LinkColumn("DOI", display_text="https://doi.org/(.*?/.*?)/")}, 
    hide_index=True,
)

# Display the data as an Altair chart using `st.altair_chart`.
# Count number of articles per year and PMID.
df_chart =  df_filtered.groupby(["Year"])['PMID'].size().reset_index(name="gross")

chart = (
    alt.Chart(df_chart)
    .mark_line()
    .encode(
        x=alt.X("Year:N", title="Year"),
        y=alt.Y("gross:Q", title="Number of Articles"),
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)
