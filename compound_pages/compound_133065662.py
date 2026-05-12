
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Antibiotic 8327A", layout="wide")
st.title("Antibiotic 8327A")
st.markdown(f"PubChem Compound ID: [133065662](https://pubchem.ncbi.nlm.nih.gov/compound/133065662)")
st.markdown(f"IUPAC Name: (1S,2R,19R,22R,34S,37R,40R,52S)-2-[(2R,3R,4R,5S,6R)-3-acetamido-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-22-amino-5,15-dichloro-64-[(2S,3R,4R,5S,6R)-3-(decanoylamino)-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-26,31,44,49-tetrahydroxy-21,35,38,54,56,59-hexaoxo-47-[(3S,4S,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-7,13,28-trioxa-20,36,39,53,55,58-hexazaundecacyclo[38.14.2.23,6.214,17.219,34.18,12.123,27.129,33.141,45.010,37.046,51]hexahexaconta-3,5,8,10,12(64),14,16,23(61),24,26,29(60),30,32,41(57),42,44,46(51),47,49,62,65-henicosaene-52-carboxylic acid")


# 4. Display the image in Streamlit
st.image(f"compound_structures/compound_133065662.jpg", caption=f"SMILES: CCCCCCCCCC(=O)N[C@H]1[C@H](Oc2c3cc4cc2Oc2ccc(cc2Cl)[C@@H](O[C@@H]2O[C@H](CO)[C@@H](O)[C@H](O)[C@H]2NC(C)=O)C2NC(=O)C(NC(=O)C4NC(=O)C4NC(=O)C(Cc5ccc(c(Cl)c5)O3)NC(=O)C(N)c3ccc(O)c(c3)Oc3cc(O)cc4c3)c3ccc(O)c(c3)-c3c(OC4O[C@H](CO)[C@@H](O)[C@H](O)[C@@H]4O)cc(O)cc3C(C(=O)O)NC2=O)O[C@H](CO)[C@@H](O)[C@@H]1O")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 133065662) ]

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

    