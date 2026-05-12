
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sarsasapogenin", layout="wide")
st.title("Sarsasapogenin")
st.markdown(f"PubChem Compound ID: [92095](https://pubchem.ncbi.nlm.nih.gov/compound/92095)")
st.markdown(f"IUPAC Name: (1R,2S,4S,5'S,6R,7S,8R,9S,12S,13S,16S,18R)-5',7,9,13-tetramethylspiro[5-oxapentacyclo[10.8.0.02,9.04,8.013,18]icosane-6,2'-oxane]-16-ol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_92095.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 92095) ]

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

    