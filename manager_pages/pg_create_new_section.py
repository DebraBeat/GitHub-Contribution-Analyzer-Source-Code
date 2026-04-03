"""
Create new section page
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="create_new_section",
    page_icon="🧊",
    layout="wide",
)

st.title("Create New Section")
st.divider()

st.markdown("Welcome, here you can create a new section if one does not exist.")

# Initialize session state list
if "section_list" not in st.session_state:
    st.session_state.section_list = []

# User input
section_name = st.text_input("Please enter the name of a section:")

# Button logic
if st.button("Add section"):

    if section_name.strip() == "":
        st.warning("Please enter a section name")

    elif section_name in st.session_state.section_list:
        st.error("Section name already exists")

    else:
        st.session_state.section_list.append(section_name)
        st.success(f"Section '{section_name}' added successfully!")

# Show existing sections
if st.session_state.section_list:
    st.subheader("Current Sections")
    st.write(st.session_state.section_list)