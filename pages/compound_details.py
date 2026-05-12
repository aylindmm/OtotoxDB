# views/compound_details.py
import streamlit as st

# Retrieve the CID from session state (set by the main page)
if "selected_cid" not in st.session_state:
    st.error("No compound selected!")
    st.page_link("pages/1_Home.py", label="Back to Home")
    st.stop()

cid = st.session_state.selected_cid

# Logic to filter your data based on this CID
st.title(f"Details for Compound: {cid}")
st.write(f"This is the dynamically generated page for PubChem CID {cid}.")

if st.button("← Back to List"):
    del st.session_state.selected_cid
    st.switch_page("pages/2_Compounds.py")