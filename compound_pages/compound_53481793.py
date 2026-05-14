
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Endotoxin", layout="wide")
st.title("Endotoxin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_53481793.jpg", width=300)
st.markdown(f"PubChem Compound ID: [53481793](https://pubchem.ncbi.nlm.nih.gov/compound/53481793)")
st.markdown(f"IUPAC Name: (2R,4R,5S,6R)-2-[(2R,4R,5S,6R)-5-[(3S,4R,5R,6R)-4-[(3S,4S,5R,6R)-4-[(3R,4S,5R,6R)-4-[(2R,3R,4S,5R,6R)-3-[(3R,4S,5R,6R)-4-[(2S,3R,4R,5R,6R)-3-acetamido-6-[[(2R,3R,4R,5S,6R)-3-acetamido-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxymethyl]-4-[(2R,3R,4R,5R,6R)-3-acetamido-5-hydroxy-6-(hydroxymethyl)-4-[(2S,3R,4S,5R,6R)-3,4,5-trihydroxy-6-[[(2S,3R,4S,5R,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxymethyl]oxan-2-yl]oxyoxan-2-yl]oxy-5-hydroxyoxan-2-yl]oxy-3-[(2R,3R,4R,5S,6R)-3-acetamido-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-5-hydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-4,5-dihydroxy-6-(hydroxymethyl)oxan-2-yl]oxy-3,5-dihydroxy-6-[[(2S,3R,4S,5R,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)oxan-2-yl]oxymethyl]oxan-2-yl]oxy-6-[(1S)-2-[(3S,4R,5S,6R)-6-[(1S)-1,2-dihydroxyethyl]-3,4-dihydroxy-5-phosphonooxyoxan-2-yl]oxy-1-hydroxyethyl]-3,5-dihydroxyoxan-2-yl]oxy-5-[[2-aminoethoxy(hydroxy)phosphoryl]oxy-hydroxyphosphoryl]oxy-6-[(1S)-1,2-dihydroxyethyl]-3-hydroxyoxan-2-yl]oxy-2-carboxy-6-[(1S)-1,2-dihydroxyethyl]-2-[[(2R,3S,4R,5R,6R)-5-[[(3R)-3-dodecanoyloxytetradecanoyl]amino]-6-[[(2R,3S,4R,5R,6R)-3-hydroxy-5-[[(3R)-3-hydroxytetradecanoyl]amino]-4-[(3R)-3-hydroxytetradecanoyl]oxy-6-phosphonooxyoxan-2-yl]methoxy]-3-phosphonooxy-4-[(3R)-3-tetradecanoyloxytetradecanoyl]oxyoxan-2-yl]methoxy]oxan-4-yl]oxy-4-[(2R,4R,5R,6R)-4-[2-aminoethoxy(hydroxy)phosphoryl]oxy-2-carboxy-6-[(1S)-1,2-dihydroxyethyl]-5-hydroxyoxan-2-yl]oxy-6-[(1S)-1,2-dihydroxyethyl]-5-hydroxyoxane-2-carboxylic acid")
st.markdown(f"Score: 0.0168435236651507")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 53481793) ]


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
        source_df[["PMID", "Year","Title", "dose", "administration_route"]].rename(columns={"PMID": "PubMed ID", 
                                                                                        "Title": "Title", 
                                                                                        "Year": "Year",
                                                                                        "dose": "Dose",
                                                                                        "administration_route": "Administration route"}),
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

tar_filtered = target_info[(target_info["PubChem_CID"] == 53481793) ]

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

    