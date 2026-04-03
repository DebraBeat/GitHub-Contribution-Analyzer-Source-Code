"""
github analyze repository webpage section.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Page configuration
st.set_page_config(
    page_title="github_analyze_repo",
    page_icon="🧊",
    layout="wide",
)

st.title("GitHub Repository Analyze Section")
st.divider()

st.markdown(
    "Welcome to the GitHub analyze repo section. Please enter a GitHub URL to analyze."
)

# Initialize session state variables
if "git_url" not in st.session_state:
    st.session_state.git_url = ""

if "section_list" not in st.session_state:
    st.session_state.section_list = []

if "analyze_clicked" not in st.session_state:
    st.session_state.analyze_clicked = False


# Input field (stored in session state)
st.session_state.git_url = st.text_input(
    "Please enter URL",
    value=st.session_state.git_url
)

# Button action
if st.button("Analyze Repository"):
    st.session_state.analyze_clicked = True


# Logic after button press
if st.session_state.analyze_clicked:

    if st.session_state.git_url.strip() != "":
        st.success(f"Analyzing Repository: {st.session_state.git_url}")

        # Processing function goes here
        st.write("Processing repository data...")

    else:
        st.warning("Please enter a GitHub URL.")
        
# displaying graph 
if 'show_graph' not in st.session_state:
    st.session_state.show_graph = False

if st.button("Generate graph"):
    st.session_state.show_graph = True
    
if st.session_state.show_graph:
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Sample Sine Wave")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")

    st.pyplot(fig)
    