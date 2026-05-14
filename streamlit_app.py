import streamlit as st
import pandas as pd
# Add a home page (your current main script)
main_page = st.Page("pages/1_Home.py", title="Home", default=True)

# Define your pages
# The 'title' is what shows in the sidebar, 'icon' is optional
compounds_page = st.Page("pages/2_Compounds.py", title="Compounds")
articles_page = st.Page("pages/3_Articles.py", title="Articles")
target_page = st.Page("pages/4_Targets.py", title="Targets")
download_page = st.Page("pages/5_Download.py", title="Download")


df = pd.read_csv("data/compounds.tsv", sep="\t")
df = df.sort_values(by="name")

# 1. Create the list of pages
compound_pages = []
for index, row in df.iterrows():
    cid = row['PubChem_CID']
    name = row['name']
    # Ensure these .py files actually exist in your 'compounds' folder!
    page = st.Page(f"compound_pages/compound_{cid}.py", title=f"{name}")
    compound_pages.append(page)
    
df2 = pd.read_csv("data/targets.tsv", sep="\t")
df2 = df2.drop_duplicates(subset='UniProt..SwissProt..Primary.ID.of.Target.Chain')  # ← here, before the loop
df2 = df2.sort_values(by="prot_name")
    
target_pages = []
for index, row in df2.iterrows():
    Uid = row['UniProt..SwissProt..Primary.ID.of.Target.Chain']
    name = row["prot_name"]
    # Ensure these .py files actually exist in your 'compounds' folder!
    page = st.Page(f"target_pages/target_{Uid}.py", title=f"{Uid}")
    target_pages.append(page)
   

# 2. Define your main app structure
# You must include the compound_pages list here
pg = st.navigation({
    "Main Menu": [
        main_page,
        compounds_page,
        articles_page,
        target_page,
        download_page
        
    ],
    "Compounds": compound_pages,
    "Targets": target_pages# This adds them to the nav bar
}, position="top")

pg.run()

