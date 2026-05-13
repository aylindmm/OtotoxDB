
import streamlit as st
import pandas as pd

st.set_page_config(page_title="N-(2-aminoethyl)-2-(4-(2-(4-((9-((2r,3r,4s,5r)-3,4-dihydroxy-5-(hydroxymethyl)tetrahydrofuran-2-yl)-9h-purin-6-yl)amino)phenyl)acetamido)phenyl)acetamide", layout="wide")
st.title("N-(2-aminoethyl)-2-(4-(2-(4-((9-((2r,3r,4s,5r)-3,4-dihydroxy-5-(hydroxymethyl)tetrahydrofuran-2-yl)-9h-purin-6-yl)amino)phenyl)acetamido)phenyl)acetamide")
# Display the image in Streamlit
st.image(f"compound_structures/compound_126054.jpg", width=300)
st.markdown(f"PubChem Compound ID: [126054](https://pubchem.ncbi.nlm.nih.gov/compound/126054)")
st.markdown(f"IUPAC Name: N-(2-aminoethyl)-2-[4-[[2-[4-[[9-[(2R,3R,4S,5R)-3,4-dihydroxy-5-(hydroxymethyl)oxolan-2-yl]purin-6-yl]amino]phenyl]acetyl]amino]phenyl]acetamide")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 126054) ]

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

    