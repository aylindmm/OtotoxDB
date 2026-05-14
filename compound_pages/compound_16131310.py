
import streamlit as st
import pandas as pd

st.set_page_config(page_title="104504-34-9", layout="wide")
st.title("104504-34-9")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16131310.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16131310](https://pubchem.ncbi.nlm.nih.gov/compound/16131310)")
st.markdown(f"IUPAC Name: (3S)-3-[[(2S)-5-amino-2-[[(2S)-2-[[(2S,3R)-2-[[(2S)-5-amino-2-[[(2S)-2-[[(2S)-2-[[(2S,3R)-2-[[(2S,3R)-2-[[(2S)-2-[[(2S)-4-amino-2-[[(2S)-2-[[(2S)-5-amino-2-[[(2S)-2-amino-4-methylsulfanylbutanoyl]amino]-5-oxopentanoyl]amino]-3-(1H-indol-3-yl)propanoyl]amino]-4-oxobutanoyl]amino]-3-hydroxypropanoyl]amino]-3-hydroxybutanoyl]amino]-3-hydroxybutanoyl]amino]-3-phenylpropanoyl]amino]-3-(4H-imidazol-4-yl)propanoyl]amino]-5-oxopentanoyl]amino]-3-hydroxybutanoyl]amino]-4-methylpentanoyl]amino]-5-oxopentanoyl]amino]-4-[(2S)-2-[[(2S)-1-[[(2S)-1-[2-[[2-[[(2S)-2-[[(2S)-1-[(2S)-2-[[(2S)-2-[[(2S)-2-[[2-[[(2S)-2-amino-5-carbamimidamidopentanoyl]amino]acetyl]amino]-4-methylpentanoyl]amino]-3-(4-hydroxyphenyl)propanoyl]amino]-3-phenylpropanoyl]pyrrolidine-2-carbonyl]amino]propanoyl]amino]acetyl]amino]acetyl]oxy-3-methyl-1-oxobutan-2-yl]amino]-5-carbamimidamido-1-oxopentan-2-yl]carbamoyl]pyrrolidin-1-yl]-4-oxobutanoic acid")
st.markdown(f"Score: 0.0168435236651507")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16131310) ]


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
    source_df = df_filtered[df_filtered['variable'] == variable]
    source_df[["PMID", "Year","Title", "dose", "administrarion_route"]].rename(columns={"PMID": "PubMed ID", 
                                                                                        "Title": "Title", 
                                                                                        "Year": "Year",
                                                                                        "dose": "Dose",
                                                                                        "administrarion_route": "Administration route"}),
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

tar_filtered = target_info[(target_info["PubChem_CID"] == 16131310) ]

tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

if tar_filtered.empty:
    st.info("No target information available for this compound.")
else:
    for variable in tar_filtered['Target.Name'].unique():
        source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
        uniid = source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]
        st.markdown(f"[{variable}](target_{uniid}/)")
        source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")

        st.markdown(f"Uniprot ID: [{source_df['prot_name'].iloc[0]}]({source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'].iloc[0]})")

        st.dataframe(
            source_df[["variable", "value"]].rename(columns={"variable": "Binding type", "value": "Value (nM)"}),
            use_container_width=True,
            hide_index=True,
        )

if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    