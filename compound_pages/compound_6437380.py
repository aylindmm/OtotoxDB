
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lumefantrine", layout="wide")
st.title("Lumefantrine")
st.markdown(f"PubChem Compound ID: [6437380](https://pubchem.ncbi.nlm.nih.gov/compound/6437380)")
st.markdown(f"IUPAC Name: 2-(dibutylamino)-1-[(9Z)-2,7-dichloro-9-[(4-chlorophenyl)methylidene]fluoren-4-yl]ethanol")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_6437380.jpg", caption=f"SMILES: CCCCN(CCCC)CC(O)c1cc(Cl)cc2c1-c1ccc(Cl)cc1C2=Cc1ccc(Cl)cc1")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6437380) ]

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

    