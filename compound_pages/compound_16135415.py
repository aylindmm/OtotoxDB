
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ziconotide", layout="wide")
st.title("Ziconotide")
# Display the image in Streamlit
st.image(f"compound_structures/compound_16135415.jpg", width=300)
st.markdown(f"PubChem Compound ID: [16135415](https://pubchem.ncbi.nlm.nih.gov/compound/16135415)")
st.markdown(f"IUPAC Name: 2-[(1R,4S,7S,13S,16R,21R,24S,27S,30S,33S,36S,39S,42R,45S,48S,54S,60S,63R,68R,71S,77S)-63-amino-13,45,54,60-tetrakis(4-aminobutyl)-4,36-bis(3-carbamimidamidopropyl)-16-carbamoyl-71-[(1R)-1-hydroxyethyl]-7,39,77-tris(hydroxymethyl)-27-[(4-hydroxyphenyl)methyl]-48-methyl-33-(2-methylpropyl)-30-(2-methylsulfanylethyl)-2,5,8,11,14,23,26,29,32,35,38,41,44,47,50,53,56,59,62,69,72,75,78,85-tetracosaoxo-18,19,65,66,81,82-hexathia-3,6,9,12,15,22,25,28,31,34,37,40,43,46,49,52,55,58,61,70,73,76,79,84-tetracosazatricyclo[40.37.4.221,68]pentaoctacontan-24-yl]acetic acid")
st.markdown(f"Score: 0.0168435236651507")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 16135415) ]


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}

import ast
df_filtered["dose"] = df_filtered["dose"].apply(lambda x: ", ".join(ast.literal_eval(x)) if isinstance(x, str) else ", ".join(x))
df_filtered["administration_route"] = df_filtered["administration_route"].apply(lambda x: ", ".join(ast.literal_eval(x)) if isinstance(x, str) else ", ".join(x))


for variable in df_filtered['variable'].unique():

    if variable == "ototoxic_drugs":

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
                "Dose": st.column_config.ListColumn(),
                "Administration route": st.column_config.ListColumn()},
            hide_index=True,
        )
    if variable == "otoprotective_drugs":
        label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
        st.markdown(f"**{label}**")
        source_df = df_filtered[df_filtered['variable'] == variable]
        st.dataframe(
            source_df[["PMID", "Year","Title"]].rename(columns={"PMID": "PubMed ID", 
                                                                                            "Title": "Title", 
                                                                                            "Year": "Year"}),
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

tar_filtered = target_info[(target_info["PubChem_CID"] == 16135415) ]

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

    