
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ifosfamide", layout="wide")
st.title("ifosfamide")
st.markdown(f"PubChem Compound ID: [3690](https://pubchem.ncbi.nlm.nih.gov/compound/3690)")
st.markdown(f"IUPAC Name: N,3-bis(2-chloroethyl)-2-oxo-1,3,2lambda5-oxazaphosphinan-2-amine")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_3690.jpg", caption=f"SMILES: O=P1(NCCCl)OCCCN1CCCl")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 3690) ]

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

    