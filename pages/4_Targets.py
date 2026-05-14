import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Targets")
st.title("Protein targets")
st.write(
    """
These are the protein targets identified for the ototoxic and otoprotective compounds.
"""
)
#st.cache_data.clear()
# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/targets.tsv", sep="\t")
    return df


df = load_data()

# Show a slider widget with the years using `st.slider`.
compound_count = st.slider("Compounds",0, 180, (0,180))


# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[ df["compound_count"].between(compound_count[0], compound_count[1])]
df_filtered = df_filtered.sort_values(by="compound_count", ascending=False)

# Convert the Uniprot column to string
df_filtered['link_to_page'] = df_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain']
df_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = df_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")  
df_filtered['link_to_page'] = df_filtered['link_to_page'].apply(lambda x: f"target_{x}/")
import ast

df_filtered["name"] = df_filtered["name"].apply(lambda x: ", ".join(ast.literal_eval(x)) if isinstance(x, str) else ", ".join(x))


# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_filtered,
    use_container_width=True,
    column_config={"Target.Name": st.column_config.TextColumn(label="Target Name"),
                   "UniProt..SwissProt..Primary.ID.of.Target.Chain": st.column_config.LinkColumn("UniProt ID", display_text="https://www.uniprot.org/uniprotkb/(.*?)/"),
                  "name": st.column_config.ListColumn(label="Compounds"),
                  "prot_name": st.column_config.TextColumn(label="Symbol"),
                  "compound_count": st.column_config.NumberColumn(label="Compounds"),
                  "link_to_page": st.column_config.LinkColumn("Details", 
                                                                      display_text=":material/open_in_new:") },               
    hide_index=True
)


st.subheader("Top 20 protein targets:")
# Display the data as an Altair chart using `st.altair_chart`.
# Count number of articles per year and PMID.

chart = (
    alt.Chart(df_filtered[:20])
    .mark_bar(color="#F08200")
    .encode(
        x=alt.X("prot_name:N", title="Protein"),
        y=alt.Y("compound_count:Q", title="Number of Compounds"),
    )
    .properties(height=320)
)
st.altair_chart(chart, use_container_width=True)
