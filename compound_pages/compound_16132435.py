
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Iberiotoxin", layout="wide")
st.title("Iberiotoxin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16132435.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16132435](https://pubchem.ncbi.nlm.nih.gov/compound/16132435)")
st.markdown(f"IUPAC Name: 5-amino-2-[[2-[[10-[[6-amino-2-[[6-amino-2-[[2-[[2-[[7,34-bis(4-aminobutyl)-37-[[2-[[2-[[2-[[10-(4-aminobutyl)-22-[[3-carboxy-2-[[2-[[3-carboxy-2-[[3-hydroxy-2-[[2-[(5-oxopyrrolidine-2-carbonyl)amino]-3-phenylpropanoyl]amino]butanoyl]amino]propanoyl]amino]-3-methylbutanoyl]amino]propanoyl]amino]-7-(2-carboxyethyl)-13,19-bis(hydroxymethyl)-6,9,12,15,18,21-hexaoxo-16-propan-2-yl-1,2-dithia-5,8,11,14,17,20-hexazacyclotricosane-4-carbonyl]amino]-3-(1H-indol-3-yl)propanoyl]amino]-3-hydroxypropanoyl]amino]-3-methylbutanoyl]amino]-25-benzyl-13-(3-carbamimidamidopropyl)-16,31-bis(carboxymethyl)-28-(2-methylpropyl)-6,9,12,15,18,21,24,27,30,33,36-undecaoxo-19-propan-2-yl-1,2-dithia-5,8,11,14,17,20,23,26,29,32,35-undecazacyclooctatriacontane-4-carbonyl]amino]-4-methylsulfanylbutanoyl]amino]acetyl]amino]hexanoyl]amino]hexanoyl]amino]-7-(3-carbamimidamidopropyl)-6,9-dioxo-1,2-dithia-5,8-diazacycloundecane-4-carbonyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-5-oxopentanoic acid")
st.markdown(f"Score: -0.0134498991257566")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16132435) ]

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

    