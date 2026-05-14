
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tubocurarine", layout="wide")
st.title("Tubocurarine")
# Display the image in Streamlit
st.image(f"compound_structures/compound_6000.jpg", width=300)
st.markdown(f"PubChem Compound ID: [6000](https://pubchem.ncbi.nlm.nih.gov/compound/6000)")
st.markdown(f"IUPAC Name: (1S,16R)-10,25-dimethoxy-15,15,30-trimethyl-7,23-dioxa-30-aza-15-azoniaheptacyclo[22.6.2.23,6.18,12.118,22.027,31.016,34]hexatriaconta-3(36),4,6(35),8(34),9,11,18(33),19,21,24,26,31-dodecaene-9,21-diol")
st.markdown(f"Score: -0.0084217618325753")
st.markdown(f"Classification: otoprotective")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 6000) ]


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

tar_filtered = target_info[(target_info["PubChem_CID"] == 6000) ]

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

    