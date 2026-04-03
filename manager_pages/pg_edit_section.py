"""
Edit section page
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="edit_section",
    page_icon="🧊",
    layout="wide",
)

st.title("Edit Section")
st.divider()

st.markdown("Welcome. Here you can edit a section that already exists.")

# Initialize session state
if "section_list" not in st.session_state:
    st.session_state.section_list = []

# Input fields
old_section = st.text_input("Please enter a section to edit")
new_section = st.text_input("Please enter new section name")

if st.button("Edit Section"):

    old_section = old_section.strip()
    new_section = new_section.strip()

    if old_section == "" or new_section == "":
        st.warning("Both fields are required")

    elif old_section not in st.session_state.section_list:
        st.error("Old section name does not exist")

    elif new_section in st.session_state.section_list:
        st.error("New section name already exists in list")

    else:
        index = st.session_state.section_list.index(old_section)
        st.session_state.section_list[index] = new_section
        st.success(f"Section '{old_section}' updated to '{new_section}'")

# Display current sections
if st.session_state.section_list:
    st.subheader("Current Sections")

    for i, section in enumerate(st.session_state.section_list, start=1):
        st.write(f"{i}. {section}")
else:
    st.info("No sections created yet.")