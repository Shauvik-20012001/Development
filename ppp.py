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
        # Regex to check for valid email format
        email_valid = re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
        if not email_valid:
            st.error("Please enter a valid email address.")
    
    # Date of Birth input (DOB)
    dob = st.date_input("Enter your date of birth:")
    
    # Center selection
    center = st.selectbox("Select your Center:", ["Center 1", "Center 2", "Center 3", "Center 4"])
    
    # Partner Name (List format)
    partner_name = st.selectbox("Select Partner Name:", ["Partner A", "Partner B", "Partner C"])
    
    # Date of Audit (Date format)
    date_of_audit = st.date_input("Enter Date of Audit:")
    
    # Week (List format)
    week = st.selectbox("Select Week:", ["Week 1", "Week 2", "Week 3", "Week 4"])
    
    # Audit Category (List format)
    audit_category = st.selectbox("Select Audit Category:", ["Category 1", "Category 2", "Category 3"])
    
    # EMP ID (Non-numeric validation)
    emp_id = st.text_input("Enter EMP ID:")
    emp_id_valid = emp_id.isnumeric() if emp_id else True
    if emp_id and not emp_id_valid:
        st.error("EMP ID should be numeric.")
    
    # Login ID (Numeric validation)
    login_id = st.text_input("Enter Login ID:")
    login_id_valid = login_id.isnumeric() if login_id else True
    if login_id and not login_id_valid:
        st.error("Login ID should be numeric.")
    
    # Agent Name (No validation)
    agent_name = st.text_input("Enter Agent Name:")
    
    # Team Leader (No validation)
    team_leader = st.text_input("Enter Team Leader Name:")
    
    # Audit Name (No validation)
    audit_name = st.text_input("Enter Audit Name:")
    
    # Auditor Center (List validation)
    auditor_center = st.selectbox("Select Auditor Center:", ["Center 1", "Center 2", "Center 3", "Center 4"])
    
    # Auditor Designation (List validation)
    auditor_designation = st.selectbox("Select Auditor Designation:", ["Designation 1", "Designation 2", "Designation 3"])
    
    # User Register Number (Numeric validation)
    user_register_number = st.text_input("Enter User Register Number:")
    user_register_number_valid = user_register_number.isnumeric() if user_register_number else True
    if user_register_number and not user_register_number_valid:
        st.error("User Register Number should be numeric.")
    
    # Calling Number (Numeric validation)
    calling_number = st.text_input("Enter Calling Number:")
    calling_number_valid = calling_number.isnumeric() if calling_number else True
    if calling_number and not calling_number_valid:
        st.error("Calling Number should be numeric.")
    
    # Date of Call (Date format validation)
    date_of_call = st.date_input("Enter Date of Call:")
    
    # Call Time Slot (Time format validation)
    call_time_slot = st.time_input("Enter Call Time Slot:")
    
    # Bucket (List format)
    bucket = st.selectbox("Select Bucket:", ["Bucket 1", "Bucket 2", "Bucket 3", "Bucket 4"])
    
    # Energetic Opening and Closing (Yes/No validation)
    energetic_opening_closing = st.selectbox("Energetic Opening and Closing?", ["Yes", "No"])
    
    # Motive of the Call (Yes/No validation)
    motive_of_call = st.selectbox("Motive of the Call?", ["Yes", "No"])
    
    # Probe / Confirm User's Profession (Yes/No validation)
    probe_confirm_user_profession = st.selectbox("Probe / Confirm User's Profession?", ["Yes", "No"])
    
    # Button to submit the form
    if st.button("Submit"):
        # Validate all fields
        
        # Email Validation
        if not email:
            st.error("Please provide your email address.")
        elif not email_valid:
            st.error("Please enter a valid email address.")
        
        # Timestamp Validation
        elif not timestamp:
            st.error("Please select a timestamp.")
        
        # Date of Birth Validation
        elif not dob:
            st.error("Please provide your date of birth.")
        
        # Center Selection Validation
        elif not center:
            st.error("Please select your center.")
        
        # EMP ID Validation
        elif not emp_id.isnumeric():
            st.error("EMP ID should be numeric.")
        
        # Login ID Validation
        elif not login_id.isnumeric():
            st.error("Login ID should be numeric.")
        
        # User Register Number Validation
        elif not user_register_number.isnumeric():
            st.error("User Register Number should be numeric.")
        
        # Calling Number Validation
        elif not calling_number.isnumeric():
            st.error("Calling Number should be numeric.")
        
        # Success Message
        else:
            # Format fields to display
            timestamp_str = timestamp.strftime('%Y-%m-%d')
            dob_str = dob.strftime('%Y-%m-%d')
            date_of_audit_str = date_of_audit.strftime('%Y-%m-%d')
            date_of_call_str = date_of_call.strftime('%Y-%m-%d')
            
            st.success(f"Form Submitted Successfully!\n"
                       f"Timestamp: {timestamp_str}\n"
                       f"Email: {email}\n"
                       f"DOB: {dob_str}\n"
                       f"Date of Audit: {date_of_audit_str}\n"
                       f"Week: {week}\n"
                       f"Audit Category: {audit_category}\n"
                       f"Partner Name: {partner_name}\n"
                       f"EMP ID: {emp_id}\n"
                       f"Login ID: {login_id}\n"
                       f"Agent Name: {agent_name}\n"
                       f"Team Leader: {team_leader}\n"
                       f"Audit Name: {audit_name}\n"
                       f"Auditor Center: {auditor_center}\n"
                       f"Auditor Designation: {auditor_designation}\n"
                       f"User Register Number: {user_register_number}\n"
                       f"Calling Number: {calling_number}\n"
                       f"Date of Call: {date_of_call_str}\n"
                       f"Call Time Slot: {call_time_slot}\n"
                       f"Bucket: {bucket}\n"
                       f"Energetic Opening and Closing: {energetic_opening_closing}\n"
                       f"Motive of the Call: {motive_of_call}\n"
                       f"Probe / Confirm User's Profession: {probe_confirm_user_profession}")

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
