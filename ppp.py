import streamlit as st

# Function to set background color
def set_background_color(color):
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background color to blue
set_background_color("#0000FF")

# Optional: Add a title or any other content to the page
st.title("Blank Page with Blue Background")
