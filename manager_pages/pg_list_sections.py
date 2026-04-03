"""
List sections page
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="list_sections",
    page_icon="🧊",
    layout="wide",
)

st.title("List Sections")
st.divider()

st.markdown(
    "Welcome, here you can view a list of all available sections that have been created."
)

# Initialize session state if it doesn't exist
if "section_list" not in st.session_state:
    st.session_state.section_list = []

if st.button("Display Sections"):

    if not st.session_state.section_list:
        st.error("No sections created, please create a section.")

    else:
        st.write("Displaying created sections:")

        for index, section in enumerate(st.session_state.section_list, start=1):
            st.write(f"{index}. {section}")