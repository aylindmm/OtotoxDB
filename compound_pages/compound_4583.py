
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ofloxacin", layout="wide")
st.title("Ofloxacin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_4583.jpg", width=300)
st.markdown(f"PubChem Compound ID: [4583](https://pubchem.ncbi.nlm.nih.gov/compound/4583)")
st.markdown(f"IUPAC Name: 7-fluoro-2-methyl-6-(4-methylpiperazin-1-yl)-10-oxo-4-oxa-1-azatricyclo[7.3.1.05,13]trideca-5(13),6,8,11-tetraene-11-carboxylic acid")
st.markdown(f"Score: 0.0806993947545393")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 4583) ]

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

    