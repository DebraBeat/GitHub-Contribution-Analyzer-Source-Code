"""
Edit user info page
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="edit_user_info",
    page_icon="🧊",
    layout="wide",
)

st.title("Edit User Info")
st.divider()

st.markdown("Welcome, here you can edit your Name, ID, and Role.")

# Initialize session state users list
if "users" not in st.session_state:
    st.session_state.users = [
        {"id": 10, "username": "Sabir", "role": "manager"},
        {"id": 22, "username": "Sabir", "role": "manager"},
        {"id": 32, "username": "Sabir", "role": "manager"},
        {"id": 42, "username": "Sabir", "role": "manager"},
    ]

# Select user to edit
user_ids = [user["id"] for user in st.session_state.users]

selected_id = st.selectbox("Select User ID to Edit", user_ids)

# Find selected user
selected_user = None
for user in st.session_state.users:
    if user["id"] == selected_id:
        selected_user = user
        break

# Editable fields
new_username = st.text_input("Edit Username", value=selected_user["username"])
new_role = st.text_input("Edit Role", value=selected_user["role"])

if st.button("Update User"):

    if new_username.strip() == "" or new_role.strip() == "":
        st.warning("All fields are required.")

    else:
        selected_user["username"] = new_username
        selected_user["role"] = new_role

        st.success("User information updated successfully!")

# Display users
st.subheader("Current Users")

df = pd.DataFrame(st.session_state.users)
st.dataframe(df, use_container_width=True)