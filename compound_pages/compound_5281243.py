
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lutein", layout="wide")
st.title("Lutein")
# Display the image in Streamlit
st.image(f"compound_structures/compound_5281243.jpg", width=300)
st.markdown(f"PubChem Compound ID: [5281243](https://pubchem.ncbi.nlm.nih.gov/compound/5281243)")
st.markdown(f"IUPAC Name: (1R)-4-[(1E,3E,5E,7E,9E,11E,13E,15E,17E)-18-[(1R,4R)-4-hydroxy-2,6,6-trimethylcyclohex-2-en-1-yl]-3,7,12,16-tetramethyloctadeca-1,3,5,7,9,11,13,15,17-nonaenyl]-3,5,5-trimethylcyclohex-3-en-1-ol")
st.markdown(f"Score: -0.0403496973772697")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5281243) ]

# Convert dataframe to CSV
csv = df_filtered.to_csv(index=False, sep='\t').encode('utf-8')

st.download_button(
    label="Download data as TSV",
    data=csv,
    file_name='articles.tsv',
    mime='text/tsv',
)


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
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

    