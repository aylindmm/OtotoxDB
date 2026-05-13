
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Locacorten-vioform", layout="wide")
st.title("Locacorten-vioform")
# Display the image in Streamlit
st.image(f"compound_structures/compound_6452749.jpg", width=300)
st.markdown(f"PubChem Compound ID: [6452749](https://pubchem.ncbi.nlm.nih.gov/compound/6452749)")
st.markdown(f"IUPAC Name: 5-chloro-7-iodoquinolin-8-ol;[2-[(6S,8S,10S,11S,13S,14S,16R,17R)-6,9-difluoro-11,17-dihydroxy-10,13,16-trimethyl-3-oxo-6,7,8,11,12,14,15,16-octahydrocyclopenta[a]phenanthren-17-yl]-2-oxoethyl] 2,2-dimethylpropanoate")
st.markdown(f"Score: 0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6452749) ]


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

    