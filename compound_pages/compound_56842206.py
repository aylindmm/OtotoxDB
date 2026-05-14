
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gc-1008", layout="wide")
st.title("Gc-1008")
# Display the image in Streamlit
st.image(f"compound_structures/compound_56842206.jpg", width=300)
st.markdown(f"PubChem Compound ID: [56842206](https://pubchem.ncbi.nlm.nih.gov/compound/56842206)")
st.markdown(f"IUPAC Name: (2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-1-[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-4-amino-2-[[(2S,3R)-2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S)-2-[[2-[[(2S)-2-[[(2S)-2-[[(2S)-4-amino-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-2-[[2-[[(2S)-2-[[(2S)-2-[[(2S)-5-amino-2-[[(2S,3S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-amino-4-methylsulfanylbutanoyl]amino]-4-methylpentanoyl]amino]-3-methylbutanoyl]amino]propanoyl]amino]propanoyl]amino]-3-methylpentanoyl]amino]-5-oxopentanoyl]amino]-3-hydroxypropanoyl]amino]propanoyl]amino]acetyl]amino]-4-methylpentanoyl]amino]-3-hydroxybutanoyl]amino]-4-carboxybutanoyl]amino]-3-hydroxybutanoyl]amino]-4-methylpentanoyl]amino]-4-oxobutanoyl]amino]-5-carbamimidamidopentanoyl]amino]-4-carboxybutanoyl]amino]acetyl]amino]-3-methylbutanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-hydroxybutanoyl]amino]-3-methylbutanoyl]amino]-3-phenylpropanoyl]amino]propanoyl]pyrrolidine-2-carbonyl]amino]-3-hydroxybutanoyl]amino]-4-oxobutanoyl]amino]-4-carboxybutanoyl]amino]propanoyl]amino]-3-phenylpropanoyl]amino]-5-carbamimidamidopentanoyl]amino]propanoyl]amino]-4-methylpentanoyl]pyrrolidine-2-carbonyl]pyrrolidine-2-carbonyl]amino]-5-carbamimidamidopentanoyl]amino]-4-carboxybutanoyl]amino]-5-carbamimidamidopentanoyl]amino]-3-hydroxypropanoyl]amino]-5-carbamimidamidopentanoyl]amino]-4-methylpentanoyl]amino]-4-methylpentanoic acid")
st.markdown(f"Score: -0.0134498991257566")
st.markdown(f"Classification: otoprotective")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56842206) ]


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
        source_df[["PMID", "Title", "Year"]].rename(columns={"PMID": "PubMed ID", "Title": "Title", "Year": "Year"}),
        use_container_width=True,
        column_config={
            "PubMed ID": st.column_config.LinkColumn("PubMed ID", display_text="https://pubmed.ncbi.nlm.nih.gov/(.*?)/"),
            "Title": st.column_config.TextColumn("Title"),
        },
        hide_index=True,
    )


st.subheader("Targets")
@st.cache_data
def load_data():
    targets_info = pd.read_csv("data/target_info.tsv", sep='\t')
    return targets_info

target_info = load_data()

tar_filtered = target_info[(target_info["PubChem_CID"] == 56842206) ]

tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

if tar_filtered.empty:
    st.info("No target information available for this compound.")
else:
    for variable in tar_filtered['Target.Name'].unique():
        source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
        uniid = source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]
        st.markdown(f"[{variable}](https://some-base-url/target_{uniid}/)")
        source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")

        st.markdown(f"Uniprot ID: [{source_df['prot_name'].iloc[0]}]({source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]})")

        st.dataframe(
            source_df[["variable", "value"]].rename(columns={"variable": "Binding type", "value": "Value (nM)"}),
            use_container_width=True,
            hide_index=True,
        )

if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    