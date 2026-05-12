
import streamlit as st
import pandas as pd

st.set_page_config(page_title="paroxetine", layout="wide")
st.title("paroxetine")
st.markdown(f"PubChem Compound ID: [43815](https://pubchem.ncbi.nlm.nih.gov/compound/43815)")
st.markdown(f"IUPAC Name: (3S,4R)-3-(1,3-benzodioxol-5-yloxymethyl)-4-(4-fluorophenyl)piperidine")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_43815.jpg", caption=f"SMILES: Fc1ccc([C@@H]2CCNC[C@H]2COc2ccc3c(c2)OCO3)cc1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 43815) ]

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

    