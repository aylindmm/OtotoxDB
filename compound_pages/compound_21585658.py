
import streamlit as st
import pandas as pd

st.set_page_config(page_title="DAPTOMYCIN", layout="wide")
st.title("DAPTOMYCIN")
st.markdown(f"PubChem Compound ID: [21585658](https://pubchem.ncbi.nlm.nih.gov/compound/21585658)")
st.markdown(f"IUPAC Name: (3S)-3-[[(2R)-4-amino-2-[[(2S)-2-(decanoylamino)-3-(1H-indol-3-yl)propanoyl]amino]-4-oxobutanoyl]amino]-4-[[(3S,6S,9R,15S,18R,21S,24S,30S,31R)-3-[2-(2-aminophenyl)-2-oxoethyl]-24-(3-aminopropyl)-15,21-bis(carboxymethyl)-6-[(2R)-1-carboxypropan-2-yl]-9-(hydroxymethyl)-18,31-dimethyl-2,5,8,11,14,17,20,23,26,29-decaoxo-1-oxa-4,7,10,13,16,19,22,25,28-nonazacyclohentriacont-30-yl]amino]-4-oxobutanoic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_21585658.jpg", caption=f"SMILES: CCCCCCCCCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)NC(CC(N)=O)C(=O)NC(CC(=O)O)C(=O)NC1C(=O)NCC(=O)NC(CCCN)C(=O)NC(CC(=O)O)C(=O)NC(C)C(=O)NC(CC(=O)O)C(=O)NCC(=O)NC(CO)C(=O)NC([C@H](C)CC(=O)O)C(=O)NC(CC(=O)c2ccccc2N)C(=O)O[C@@H]1C")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 21585658) ]

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

    