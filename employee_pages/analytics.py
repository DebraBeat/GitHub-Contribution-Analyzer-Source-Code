import streamlit as st

st.title("Section Analytics")
st.write("Run analytical tools on your assigned repositories.")

# Find assigned sections
assigned_sections = []
if "sections" in st.session_state:
    user_id = st.session_state.user_info["id"]
    for sec, data in st.session_state.sections.items():
        if any(user_id in member for member in data["members"]):
            assigned_sections.append({"name": sec, "url": data["url"]})

if not assigned_sections:
    st.warning("You must be assigned to a section to view analytics here. Use the Public Tools instead.")
else:
    sec_options = {sec["name"]: sec["url"] for sec in assigned_sections}
    selected_sec_name = st.selectbox("Select a Section:", list(sec_options.keys()))
    repo_url = sec_options[selected_sec_name]
    
    st.write(f"**Target Repository:** {repo_url}")
    
    tool_choice = st.selectbox(
        "Choose an Analytical Tool:",
        [
            "Activity Histograms (Time/Day)",
            "Word Cloud (Commit Messages)",
            "Contribution Line Charts (Repo)",
            "Top Users Bar Chart (Repo)"
        ]
    )

    if st.button("Generate Analysis"):
        st.success(f"Running {tool_choice} for {selected_sec_name}...")
        st.info("Visualization placeholder.")