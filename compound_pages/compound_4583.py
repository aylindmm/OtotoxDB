
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ofloxacin", layout="wide")
st.title("ofloxacin")
st.markdown(f"PubChem Compound ID: [4583](https://pubchem.ncbi.nlm.nih.gov/compound/4583)")
st.markdown(f"IUPAC Name: 7-fluoro-2-methyl-6-(4-methylpiperazin-1-yl)-10-oxo-4-oxa-1-azatricyclo[7.3.1.05,13]trideca-5(13),6,8,11-tetraene-11-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_4583.jpg", caption=f"SMILES: CC1COc2c(N3CCN(C)CC3)c(F)cc3c(=O)c(C(=O)O)cn1c23")

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

    