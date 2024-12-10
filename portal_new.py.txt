import streamlit as st

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
    
    # Text input
    user_name = st.text_input("Enter your name:")
    
    # Number input
    user_age = st.number_input("Enter your age:", min_value=0)
    
    # Button to submit the form
    if st.button("Submit"):
        if user_name and user_age:
            st.success(f"Hello, {user_name}! You are {user_age} years old.")
        else:
            st.error("Please provide both name and age.")

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
