import streamlit as st
# Show the page title and description.
st.set_page_config(page_title="OtotoxDB")
st.title("Otoactive Compounds Data Base")
st.write(
    """
    Welcome to the OtotoxDB, a comprehensive database of compounds that have been shown to have ototoxic effects.
    This database is designed to provide researchers, clinicians, and students with easy access to information about ototoxic compounds, including their chemical properties, mechanisms of action, and associated research articles.
    
    The database was built using Large Language Models (LLMs) to extract and organize data from scientific literature, ensuring that the information is up-to-date and accurate. We hope that OtotoxDB will serve as a valuable resource for those studying ototoxicity and related fields.
    
    """
)


st.divider()

# Navigation Cards
st.subheader("Explore the Database")
st.write("Choose a section to get started:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("###  Compounds")
    st.caption("Browse all ototoxic compounds and their chemical properties.")
    if st.button("Go to Compounds", use_container_width=True):
        st.switch_page("pages/2_Compounds.py")

with col2:
    st.markdown("### Articles")
    st.caption("Explore the scientific literature behind the database.")
    if st.button("Go to Articles", use_container_width=True):
        st.switch_page("pages/3_Articles.py")

with col3:
    st.markdown("###  Targets")
    st.caption("Browse molecular targets associated with ototoxicity.")
    if st.button("Go to Targets", use_container_width=True):
        st.switch_page("pages/4_Targets.py")

with col4:
    st.markdown("###  Download")
    st.caption("Download the full database for offline use.")
    if st.button("Go to Download", use_container_width=True):
        st.switch_page("pages/5_Download.py")

st.divider()

st.divider()
col2, col3 = st.columns(2)

with col2:
    st.caption("**Universidad Autónoma Metropolitana** \n  Unidad Cuajimalpa")
with col3:
    st.caption("**Contact:** \n adelmoral@cua.uam.mx")