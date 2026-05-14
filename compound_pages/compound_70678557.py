
import streamlit as st
import pandas as pd

st.set_page_config(page_title="9004-10-8", layout="wide")
st.title("9004-10-8")
# Display the image in Streamlit
st.image(f"compound_structures/compound_70678557.jpg", width=300)
st.markdown(f"PubChem Compound ID: [70678557](https://pubchem.ncbi.nlm.nih.gov/compound/70678557)")
st.markdown(f"IUPAC Name: (4S)-4-[[2-[[(1R,6R,12S,15S,18S,21S,24S,27S,30S,33S,36S,39S,42R,47R,50S,53S,56S,59S,62S,65S,68S,71S,74S,77S,80S,83S,88R)-88-[[(2S)-5-amino-2-[[(2S)-2-[[(2S)-2-[[(2S,3R)-2-[(2-aminoacetyl)amino]-3-methylpentanoyl]amino]-3-methylbutanoyl]amino]-4-carboxybutanoyl]amino]-5-oxopentanoyl]amino]-6-[[(2S)-2-[[(2S)-2-[[(2S)-5-amino-2-[[(2S)-3-amino-2-[[(2S)-2-[[(2S)-2-amino-3-phenylpropanoyl]amino]-3-methylbutanoyl]amino]-3-oxopropanoyl]amino]-5-oxopentanoyl]amino]-3-(1H-imidazol-4-yl)propanoyl]amino]-4-methylpentanoyl]amino]-47-[[(1S)-3-amino-1-carboxy-3-oxopropyl]carbamoyl]-53-(2-amino-2-oxoethyl)-62-(3-amino-3-oxopropyl)-77-[(2R)-butan-2-yl]-24,56-bis(2-carboxyethyl)-83-[(1S)-1-hydroxyethyl]-12,71,80-tris(hydroxymethyl)-33,50,65-tris[(4-hydroxyphenyl)methyl]-15-(1H-imidazol-4-ylmethyl)-27-methyl-18,30,36,59,68-pentakis(2-methylpropyl)-7,10,13,16,19,22,25,28,31,34,37,40,49,52,55,58,61,64,67,70,73,76,79,82,85,87-hexacosaoxo-21,39-di(propan-2-yl)-3,4,44,45,90,91-hexathia-8,11,14,17,20,23,26,29,32,35,38,41,48,51,54,57,60,63,66,69,72,75,78,81,84,86-hexacosazabicyclo[72.11.7]dononacontane-42-carbonyl]amino]acetyl]amino]-5-[[(2S)-1-[[2-[[(2S)-1-[[(2S)-1-[[(2S)-1-[[(2S,3S)-1-[(2S)-2-[[(2S)-6-amino-1-[[(1S,2S)-1-carboxy-2-hydroxypropyl]amino]-1-oxohexan-2-yl]carbamoyl]pyrrolidin-1-yl]-3-hydroxy-1-oxobutan-2-yl]amino]-3-(4-hydroxyphenyl)-1-oxopropan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-1-oxo-3-phenylpropan-2-yl]amino]-2-oxoethyl]amino]-5-carbamimidamido-1-oxopentan-2-yl]amino]-5-oxopentanoic acid")
st.markdown(f"Score: -0.0084217618325753")
st.markdown(f"Classification: otoprotective")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 70678557) ]


df_filtered['PMID'] = df_filtered['PMID'].apply(lambda x: f"https://pubmed.ncbi.nlm.nih.gov/{x}/")  

variable_labels = {
    "ototoxic_drugs": "Ototoxic Reports",
    "otoprotective_drugs": "Otoprotective Reports",
}


for variable in df_filtered['variable'].unique():

    label = variable_labels.get(variable, variable)  # falls back to raw name if not in dict
    st.markdown(f"**{label}**")
    source_df = df_filtered[df_filtered['variable'] == variable]

    import ast
    df_filtered["dose"] = df_filtered["dose"].apply(lambda x: ", ".join(ast.literal_eval(x)) if isinstance(x, str) else ", ".join(x))
    df_filtered["administration_route"] = df_filtered["administration_route"].apply(lambda x: ", ".join(ast.literal_eval(x)) if isinstance(x, str) else ", ".join(x))

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

tar_filtered = target_info[(target_info["PubChem_CID"] == 70678557) ]

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

    