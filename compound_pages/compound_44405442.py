
import streamlit as st
import pandas as pd

st.set_page_config(page_title="L-amb", layout="wide")
st.title("L-amb")
st.markdown(f"PubChem Compound ID: [44405442](https://pubchem.ncbi.nlm.nih.gov/compound/44405442)")
st.markdown(f"IUPAC Name: (1R,3S,5R,6R,9R,11R,15S,16R,17R,18S,19E,21E,23E,25E,27E,29E,31E,33R,35S,36R,37S)-33-[(2S,3R,4R,5R,6S)-4-amino-3,5-dihydroxy-6-methyloxan-2-yl]oxy-1,3,5,6,9,11,17,37-octahydroxy-15,16,18-trimethyl-13-oxo-14,39-dioxabicyclo[33.3.1]nonatriaconta-19,21,23,25,27,29,31-heptaene-36-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_44405442.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 44405442) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

for variable in df_filtered['variable'].unique():
    st.markdown(f"**{variable}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    st.dataframe(
        source_df[["PMID", "Title"]].rename(columns={"PMID": "PubMed ID", "Title": "Title"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    