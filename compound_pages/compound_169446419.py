
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Skqr1", layout="wide")
st.title("Skqr1")
# Display the image in Streamlit
st.image(f"compound_structures/compound_169446419.jpg", width=300)
st.markdown(f"PubChem Compound ID: [169446419](https://pubchem.ncbi.nlm.nih.gov/compound/169446419)")
st.markdown(f"IUPAC Name: [9-[2-[10-(2,5-dihydroxy-3,4-dimethylphenyl)decoxycarbonyl]phenyl]-6-(ethylamino)-2,7-dimethylxanthen-3-ylidene]-ethylazanium hydroxide")
st.markdown(f"Score: -0.0268997982515131")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 169446419) ]


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
        source_df[["PMID", "Title", "Year"]].rename(columns={"PMID": "PubMed ID", "Title": "Title", "Year": "Year"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    