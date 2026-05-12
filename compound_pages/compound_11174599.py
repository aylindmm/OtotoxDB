
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tetrodotoxin", layout="wide")
st.title("Tetrodotoxin")
st.markdown(f"PubChem Compound ID: [11174599](https://pubchem.ncbi.nlm.nih.gov/compound/11174599)")
st.markdown(f"IUPAC Name: (1R,5R,6R,7R,9S,11S,12S,13S,14S)-3-amino-14-(hydroxymethyl)-8,10-dioxa-2,4-diazatetracyclo[7.3.1.17,11.01,6]tetradec-3-ene-5,9,12,13,14-pentol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_11174599.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 11174599) ]

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

    