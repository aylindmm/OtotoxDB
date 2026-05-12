
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Glycyrrhizic acid", layout="wide")
st.title("Glycyrrhizic acid")
st.markdown(f"PubChem Compound ID: [14982](https://pubchem.ncbi.nlm.nih.gov/compound/14982)")
st.markdown(f"IUPAC Name: (2S,3S,4S,5R,6R)-6-[(2S,3R,4S,5S,6S)-2-[[(3S,4aR,6aR,6bS,8aS,11S,12aR,14aR,14bS)-11-carboxy-4,4,6a,6b,8a,11,14b-heptamethyl-14-oxo-2,3,4a,5,6,7,8,9,10,12,12a,14a-dodecahydro-1H-picen-3-yl]oxy]-6-carboxy-4,5-dihydroxyoxan-3-yl]oxy-3,4,5-trihydroxyoxane-2-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_14982.jpg", width=400)

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 14982) ]

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

    