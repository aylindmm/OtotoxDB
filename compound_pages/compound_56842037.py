
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Charybdotoxin", layout="wide")
st.title("Charybdotoxin")
# Display the image in Streamlit
st.image(f"compound_structures/compound_56842037.jpg", width=300)
st.markdown(f"PubChem Compound ID: [56842037](https://pubchem.ncbi.nlm.nih.gov/compound/56842037)")
st.markdown(f"IUPAC Name: (2S)-3-hydroxy-2-[[(2S)-3-(4-hydroxyphenyl)-2-[[(1R,4S,7R,12R,15S,18S,21S,24S,27S,30S,33S,36S,42S,45R,50R,53S,56S,59S,62S,65S,68R,75S,78S,81S,84S,89S,92S,95S)-42,62,75,78-tetrakis(4-aminobutyl)-50-[[(2S)-2-[[(2S)-2-[[(2S)-4-amino-2-[[(2S,3R)-3-hydroxy-2-[[(2S)-2-[[(2S)-5-oxopyrrolidine-2-carbonyl]amino]-3-phenylpropanoyl]amino]butanoyl]amino]-4-oxobutanoyl]amino]-3-methylbutanoyl]amino]-3-hydroxypropanoyl]amino]-27,81-bis(2-amino-2-oxoethyl)-15-(3-amino-3-oxopropyl)-4,18,36-tris(3-carbamimidamidopropyl)-65-(2-carboxyethyl)-30,53,56-tris[(1R)-1-hydroxyethyl]-33,59,92-tris(hydroxymethyl)-24-(1H-imidazol-5-ylmethyl)-89-(1H-indol-3-ylmethyl)-21-(2-methylpropyl)-84-(2-methylsulfanylethyl)-2,5,13,16,19,22,25,28,31,34,37,40,43,51,54,57,60,63,66,74,77,80,83,86,87,90,93,96-octacosaoxo-95-propan-2-yl-9,10,47,48,70,71-hexathia-3,6,14,17,20,23,26,29,32,35,38,41,44,52,55,58,61,64,67,73,76,79,82,85,88,91,94,97-octacosazatricyclo[43.27.14.1112,68]heptanonacontane-7-carbonyl]amino]propanoyl]amino]propanoic acid")
st.markdown(f"Score: 0.0084217618325753")
st.markdown(f"Classification: ototoxic")

st.write("---")

st.subheader("References")

@st.cache_data
def load_data():
    sources = pd.read_csv("data/articles.tsv", sep='\t')
    return sources


sources = load_data()

df_filtered = sources[(sources["PubChem_CID"] == 56842037) ]


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

tar_filtered = target_info[(target_info["PubChem_CID"] == 56842037) ]

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

    