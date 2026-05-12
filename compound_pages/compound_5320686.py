
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tiliroside", layout="wide")
st.title("Tiliroside")
st.markdown(f"PubChem Compound ID: [5320686](https://pubchem.ncbi.nlm.nih.gov/compound/5320686)")
st.markdown(f"IUPAC Name: [(2R,3S,4S,5R,6S)-6-[5,7-dihydroxy-2-(4-hydroxyphenyl)-4-oxochromen-3-yl]oxy-3,4,5-trihydroxyoxan-2-yl]methyl (E)-3-(4-hydroxyphenyl)prop-2-enoate")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_5320686.jpg", caption=f"SMILES: O=C(C=Cc1ccc(O)cc1)OC[C@H]1O[C@@H](Oc2c(-c3ccc(O)cc3)oc3cc(O)cc(O)c3c2=O)[C@H](O)[C@@H](O)[C@@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 5320686) ]

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

    