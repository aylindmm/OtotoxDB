
import streamlit as st
import pandas as pd

st.set_page_config(page_title="OXYTOCIN", layout="wide")
st.title("OXYTOCIN")
st.markdown(f"PubChem Compound ID: [439302](https://pubchem.ncbi.nlm.nih.gov/compound/439302)")
st.markdown(f"IUPAC Name: (2S)-1-[(4R,7S,10S,13S,16S,19R)-19-amino-7-(2-amino-2-oxoethyl)-10-(3-amino-3-oxopropyl)-13-[(2S)-butan-2-yl]-16-[(4-hydroxyphenyl)methyl]-6,9,12,15,18-pentaoxo-1,2-dithia-5,8,11,14,17-pentazacycloicosane-4-carbonyl]-N-[(2S)-1-[(2-amino-2-oxoethyl)amino]-4-methyl-1-oxopentan-2-yl]pyrrolidine-2-carboxamide")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_439302.jpg", caption=f"SMILES: CC[C@H](C)C1NC(=O)C(Cc2ccc(O)cc2)NC(=O)C(N)CSSCC(C(=O)N2CCCC2C(=O)NC(CC(C)C)C(=O)NCC(N)=O)NC(=O)C(CC(N)=O)NC(=O)C(CCC(N)=O)NC1=O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 439302) ]

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

    