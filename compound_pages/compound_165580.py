
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Paromomycin", layout="wide")
st.title("Paromomycin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_165580.jpg", width=300)
st.markdown(f"PubChem Compound ID: [165580](https://pubchem.ncbi.nlm.nih.gov/compound/165580)")
st.markdown(f"IUPAC Name: (2S,3S,4R,5R,6R)-5-amino-2-(aminomethyl)-6-[(2R,3S,4R,5S)-5-[(1R,2R,3S,5R,6S)-3,5-diamino-2-[(2S,3R,4R,5S,6R)-3-amino-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-6-hydroxycyclohexyl]oxy-4-hydroxy-2-(hydroxymethyl)oxolan-3-yl]oxyoxane-3,4-diol")
st.markdown(f"Score: 0.0941492938802959")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 165580) ]

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

    