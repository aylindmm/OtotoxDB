
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Coenzyme Q10", layout="wide")
st.title("Coenzyme Q10")
st.markdown(f"PubChem Compound ID: [5281915](https://pubchem.ncbi.nlm.nih.gov/compound/5281915)")
st.markdown(f"IUPAC Name: 2-[(2E,6E,10E,14E,18E,22E,26E,30E,34E)-3,7,11,15,19,23,27,31,35,39-decamethyltetraconta-2,6,10,14,18,22,26,30,34,38-decaenyl]-5,6-dimethoxy-3-methylcyclohexa-2,5-diene-1,4-dione")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5281915.jpg", caption=f"SMILES: COc1c(O)c(C)c(C=CC(C)=CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)CCC=C(C)C)c(O)c1OC")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5281915) ]

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

    