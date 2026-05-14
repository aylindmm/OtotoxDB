
import streamlit as st
import pandas as pd

st.set_page_config(page_title="VGFR3", layout="wide")
st.title("Vascular endothelial growth factor receptor 3")
st.markdown(f"Uniprot ID: [P35916](https://www.uniprot.org/uniprotkb/P35916/)")
st.markdown(f"Protein symbol: VGFR3")


st.write("---")

st.subheader("Compounds")

@st.cache_data
def load_data():
    targets_info = pd.read_csv("data/target_info.tsv", sep='\t')
    return targets_info

target_info = load_data()
compounds = pd.read_csv("data/compounds.tsv", sep='\t')

tar_filtered = target_info[(target_info['UniProt..SwissProt..Primary.ID.of.Target.Chain'] == 'P35916') ]

tar_filtered = tar_filtered.loc[:,("PubChem_CID","variable", 'value') ]

if tar_filtered.empty:
    st.info("No compound information available for this target.")
else:
    for variable in tar_filtered['PubChem_CID'].unique():
        st.markdown(f"**{variable}**")
        source_df = tar_filtered[tar_filtered['PubChem_CID'] == variable]

        compound_name = compounds[compounds['PubChem_CID'] == variable]['name'].iloc[0]
        st.markdown(f"Compound name: [{compound_name}](compound_{variable})")

        pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/compound/{variable}" if pd.notnull(variable) else "#"
        st.markdown(f"PubChem CID: [{variable}]({pubchem_url})")

        # Compound class
        compound_class = compounds[compounds['PubChem_CID'] == variable]['class'].iloc[0]
        st.markdown(f"Compound class: **{compound_class}**")

        if not source_df.empty:
            st.dataframe(
                source_df[["variable", "value"]].rename(columns={"variable": "Binding type", "value": "Value (nM)"}),
                use_container_width=True,
                hide_index=True,
            )

if st.button("Back"):
    st.switch_page("pages/1_Home.py")
    