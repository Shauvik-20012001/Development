import streamlit as st
import re
from datetime import datetime

# Title of the portal
st.title("Welcome to the Portal")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose a page:",
    ["Home", "User Input", "About"]
)

# Home Page
if page == "Home":
    st.header("Home Page")
    st.write("This is a simple portal built using Streamlit.")
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=300)
    st.write("Explore different sections from the sidebar!")

# User Input Page
elif page == "User Input":
    st.header("User Input Page")
    
    # Timestamp field (with validation for date format)
    timestamp = st.date_input("Select Timestamp:")
    
    # Email Address input (with basic validation using regex)
    email = st.text_input("Enter your email address:")
    email_valid = False
    if email:
        email_valid = re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
        if not email_valid:
            st.error("Please enter a valid email address.")
    
    # Date of Birth input (DOB)
    dob = st.date_input("Enter your date of birth:")
    
    # Center selection
    center = st.selectbox("Select your Center:", ["Center 1", "Center 2", "Center 3", "Center 4"])
    
    # Button to submit the form
    if st.button("Submit"):
        # Validation for all fields
        if not email:
            st.error("Please provide your email address.")
        elif not email_valid:
            st.error("Please enter a valid email address.")
        elif not timestamp:
            st.error("Please select a timestamp.")
        elif not dob:
            st.error("Please provide your date of birth.")
        elif not center:
            st.error("Please select your center.")
        else:
            # If everything is valid, show success message
            timestamp_str = timestamp.strftime('%Y-%m-%d')
            dob_str = dob.strftime('%Y-%m-%d')
            st.success(f"Form Submitted Successfully!\n"
                       f"Timestamp: {timestamp_str}\n"
                       f"Email: {email}\n"
                       f"DOB: {dob_str}\n"
                       f"Center: {center}")

# About Page
elif page == "About":
    st.header("About the Portal")
    st.write("""
    This portal is a simple demonstration of how to build an interactive web app 
    using Streamlit. It allows you to create various pages and interact with them 
    via user input.
    """)

# To run this app, use the following command in the terminal:
# streamlit run app.py
