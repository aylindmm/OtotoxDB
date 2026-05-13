
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transforming growth factor alpha (human)", layout="wide")
st.title("Transforming growth factor alpha (human)")
# Display the image in Streamlit
st.image(f"compound_structures/compound_121494106.jpg", width=300)
st.markdown(f"PubChem Compound ID: [121494106](https://pubchem.ncbi.nlm.nih.gov/compound/121494106)")
st.markdown(f"IUPAC Name: (4S)-4-[[(4R,7S,10S,16S,19S,25S,28S,31R)-31-[[(2S)-2-[[(1R,6R,9S,12S,18S,21S,24S,27S,30S,33S,36S,39S,42R,47R,53S,56S,59S,62S,65S,68S,71S,76S,79S,85S)-47-[[(2S)-2-[[(2S)-4-amino-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-[[(2S)-2-amino-3-methylbutanoyl]amino]-3-methylbutanoyl]amino]-3-hydroxypropanoyl]amino]-3-(1H-imidazol-4-yl)propanoyl]amino]-3-phenylpropanoyl]amino]-4-oxobutanoyl]amino]-3-carboxypropanoyl]amino]-18-(4-aminobutyl)-27,68-bis(3-amino-3-oxopropyl)-36,71,76-tribenzyl-39-(3-carbamimidamidopropyl)-24-(2-carboxyethyl)-21,56-bis(carboxymethyl)-65,85-bis[(1R)-1-hydroxyethyl]-59-(hydroxymethyl)-62,79-bis(1H-imidazol-4-ylmethyl)-9-methyl-33-(2-methylpropyl)-8,11,17,20,23,26,29,32,35,38,41,48,54,57,60,63,66,69,72,74,77,80,83,86-tetracosaoxo-30-propan-2-yl-3,4,44,45-tetrathia-7,10,16,19,22,25,28,31,34,37,40,49,55,58,61,64,67,70,73,75,78,81,84,87-tetracosazatetracyclo[40.31.14.012,16.049,53]heptaoctacontane-6-carbonyl]amino]-3-methylbutanoyl]amino]-7-(3-carbamimidamidopropyl)-25-(hydroxymethyl)-19-[(4-hydroxyphenyl)methyl]-28-(1H-imidazol-4-ylmethyl)-10-methyl-6,9,12,15,18,21,24,27,30-nonaoxo-16-propan-2-yl-1,2-dithia-5,8,11,14,17,20,23,26,29-nonazacyclodotriacontane-4-carbonyl]amino]-5-[[(2S)-1-[[(2S)-1-[[(2S)-3-carboxy-1-[[(2S)-1-[[(2S)-1-[[(1S)-1-carboxyethyl]amino]-4-methyl-1-oxopentan-2-yl]amino]-4-methyl-1-oxopentan-2-yl]amino]-1-oxopropan-2-yl]amino]-1-oxopropan-2-yl]amino]-3-(1H-imidazol-4-yl)-1-oxopropan-2-yl]amino]-5-oxopentanoic acid")
st.markdown(f"Score: -0.0403496973772697")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 121494106) ]


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

tar_filtered = target_info[(target_info["PubChem_CID"] == 121494106) ]

tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'] = tar_filtered['UniProt..SwissProt..Primary.ID.of.Target.Chain'].apply(lambda x: f"https://www.uniprot.org/uniprotkb/{x}/")  
tar_filtered = tar_filtered.loc[:,('Target.Name', 'prot_name','UniProt..SwissProt..Primary.ID.of.Target.Chain', "variable", 'value') ]

for variable in tar_filtered['Target.Name'].unique():

    st.markdown(f"**{variable}**")
    source_df = tar_filtered[tar_filtered['Target.Name'] == variable]
    st.markdown(f"Uniprot ID: [source_df['prot_name'][0]](source_df['UniProt..SwissProt..Primary.ID.of.Target.Chain'][0])")
    st.dataframe(
        source_df[["variable", "value"]].rename(columns={"Variable": "Binding type", "value": "value"}),
        use_container_width=True,
        hide_index=True,
    )



if st.button("Back"):
    st.switch_page("pages/1_Home.py")

    