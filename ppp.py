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
    
    # Date of Birth input (DOB)
    LOB = st.selectbox("Select your Center:", ["SE", "SIB", "SIC", "Student"])
    
    # Center selection
    center = st.selectbox("Select your Center:", ["Bhopal", "Indore", "Vijaywada", "MYS", "Noida", "Kolkata", "Coimbatore", "Ranchi"])
    
    # Partner Name (List format)
    partner_name = st.selectbox("Select Partner Name:", ["Tarus", "TTBS", "MAGNUM", "ICCS", "INHOUSE", "HRH NEXT", "AYUDA"])
    
    # Date of Audit (Date format)
    date_of_audit = st.date_input("Enter Date of Audit:")
    
    # Week (List format)
    week = st.selectbox("Select Week:", ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"])
    
    # Audit Category (List format)
    audit_category = st.selectbox("Select Audit Category:", ["Floor", "RCA"])
    
    # EMP ID (Non-numeric validation)
    emp_id = st.text_input("Enter EMP ID:")
    
    # Login ID (Numeric validation)
    login_id = st.text_input("Enter Login ID:")
    
    # Agent Name (No validation)
    agent_name = st.text_input("Enter Agent Name:")
    
    # Team Leader (No validation)
    team_leader = st.text_input("Enter Team Leader Name:")
    
    # Audit Name (No validation)
    audit_name = st.text_input("Enter Audit Name:")
    
    # Auditor Center (List validation)
    auditor_center = st.selectbox("Select Auditor Center:", ["Indore", "Vijaywada", "Mysore", "Bhopal", "Noida", "Kolkata", "Coimbatore", "HYD", "Ranchi"])
    
    # Auditor Designation (List validation)
    auditor_designation = st.selectbox("Select Auditor Designation:", ["TL", "Trainer"])
    
    # User Register Number (Numeric validation)
    user_register_number = st.text_input("Enter User Register Number:")
    
    # Calling Number (Numeric validation)
    calling_number = st.text_input("Enter Calling Number:")
    
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
    probe_confirm_user_profession = st.selectbox("Probe / Confirm User's Profession?", ["Yes", "No", "NA"])

    # Current Profile Stage / Previous Interaction
    Current_Profile_Stage_Previous_Interaction = st.selectbox("Current Profile Stage / Previous Interaction", ["Yes", "No", "FATAL"])

    Probe_If_User_have_any_doc_releated_Profession_Study_Business = st.selectbox("Current Profile Stage / Previous Interaction", ["Yes", "No", "NA"])

    Guide_User_with_required_documents_One_by_one = st.selectbox("Current Profile Stage / Previous Interaction", ["Yes", "Fatal", "NA"])

    Urgency = st.selectbox("Urgency", ["Yes", "Fatal", "NA"])

    Objection_Handling = st.selectbox("Objection Handling", ["Yes", "Fatal", "NA"])

    Explained_user_how_to_take_first_loan = st.selectbox("Explained user how to take first loan", ["Yes", "Fatal", "NA"])

    Reconfirmation_Call_back_script = st.selectbox("Reconfirmation / Call back script", ["Yes", "Fatal", "NA"])

    Two_way_communication = st.selectbox("Two way communication", ["Yes", "NO"])

    Active_listening_and_Dead_Air = st.selectbox("Active listening and Dead Air", ["Yes", "NO"])

    Professional_Communication = st.selectbox("Professional Communication", ["Yes", "NO"])

    Information = st.selectbox("Information", ["Yes", "NO"])

    Follow_Up = st.selectbox("Follow Up", ["Yes", "NO"])

    Tagging = st.selectbox("Tagging", ["Yes", "NA", "NO"])

    Fatal = st.selectbox("Fatal", ["Yes", "NO"])

    Remarks = st.text_input("Remarks:")

    Agent_Feedback_Status = st.selectbox("Agent Feedback Status", ["Closed", "Open"])

    Profile_completion_status_prior_to_call = st.selectbox("Profile completion status prior to call", ["Blank profile", "Partially complete", "Almost complete"])

    PIP_SFA_Status = st.selectbox("PIP/SFA Status", ["Correct", "Incorrect", "NA"])

    VOC = st.text_input("VOC")

    AOI = st.text_input("AOI")
    
    call_duration = st.text_input("Enter Call Duration (HH:mm:ss):")
    
    KYC_type = st.selectbox("KYC Type", ["Not Updated", "OKYC", "VKYC", "CKYC"])

    Disposition_Accuracy = st.selectbox("Disposition Accuracy", ["Correct", "Incorrect", "Not Done"])

    DCS_Tagging_L1 = st.text_input("Enter DCS Tagging L1")

    DCS_Tagging_L2 = st.text_input("Enter DCS Tagging L2")

    DCS_Tagging_L3 = st.text_input("Enter DCS Tagging L3")

    Actual_Tagging_L1 = st.text_input("Actual Tagging L1")

    Actual_Tagging_L2 = st.text_input("Actual Tagging L2")

    Actual_Tagging_L3 = st.text_input("Actual Tagging L3")

    # Button to submit the form
    if st.button("Submit"):
        errors = []
        
        # Validate each field
        if not timestamp:
            errors.append("Please select a timestamp.")
        
        if not email or not email_valid:
            errors.append("Please provide a valid email address.")
        
        if not emp_id or not emp_id.isnumeric():
            errors.append("EMP ID should be numeric.")
        
        if not login_id or not login_id.isnumeric():
            errors.append("Login ID should be numeric.")
        
        if not user_register_number or not user_register_number.isnumeric():
            errors.append("User Register Number should be numeric.")
        
        if not calling_number or not calling_number.isnumeric():
            errors.append("Calling Number should be numeric.")
        
        if not date_of_call:
            errors.append("Please select a date of call.")
        
        if not call_time_slot:
            errors.append("Please select a call time slot.")
        
        if not remarks:
            errors.append("Please provide remarks.")
        
        # If there are errors, display them
        if errors:
            for error in errors:
                st.error(error)
        else:
            # If no errors, submit the data
            timestamp_str = timestamp.strftime('%Y-%m-%d')
            date_of_audit_str = date_of_audit.strftime('%Y-%m-%d')
            date_of_call_str = date_of_call.strftime('%Y-%m-%d')
            
            st.success(f"Form Submitted Successfully!\n"
                       f"Timestamp: {timestamp_str}\n"
                       f"Email: {email}\n"
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
                       f"Motivating Call: {motive_of_call}\n"
                       f"Probe / Confirm User's Profession: {probe_confirm_user_profession}\n"
                       f"Current Profile Stage / Previous Interaction:{Current_Profile_Stage_Previous_Interaction}\n"
                       f"Current Profile Stage / Previous Interaction:{Probe_If_User_have_any_doc_releated_Profession_Study_Business}\n"
                       f"Guide User with Required Documnets One by One:{Guide_User_with_required_documents_One_by_one}\n"
                       f"Urgency:{Urgency}\n"
                       f"Objection Handling:{Objection_Handling}\n"
                       f"Explained user how to take first loan:{Explained_user_how_to_take_first_loan}\n"
                       f"Reconfirmation Call back script:{Reconfirmation_Call_back_script}\n"
                       f"Two way communication:{Two_way_communication}\n"
                       f"Active listening and Dead Air:{Active_listening_and_Dead_Air}\n"
                       f"Professional Communication:{Professional_Communication}\n"
                       f"Information:{Information}\n"
                       f"Follow_Up:{Follow_Up}\n"
                       f"Tagging:{Tagging}\n"
                       f"Fatal:{Fatal}\n"
                       f"Remarks:{Remarks}\n"
                       f"Agent Feedback Status:{Agent_Feedback_Status}\n"
                       f"Profile completion status prior to call:{Profile_completion_status_prior_to_call}\n"
                       f"PIP/SFA_Status:{PIP_SFA_Status}\n"
                       f"VOC:{VOC}\n"
                       f"AOI:{AOI}\n"
                       f"call duration:{call_duration}\n"
                       f"KYC type:{KYC_type}\n"
                       f"Disposition Accuracy:{Disposition_Accuracy}\n"
                       f"DCS Tagging L1:{DCS_Tagging_L1}\n"
                       f"DCS Tagging L2:{DCS_Tagging_L2}\n"
                       f"DCS Tagging L2:{DCS_Tagging_L2}\n"
                       f"Actual Tagging L1:{Actual_Tagging_L1}\n"
                       f"Actual Tagging L2:{Actual_Tagging_L2}\n"
                       f"Actual Tagging L3:{Actual_Tagging_L3}\n"
            )

# About Page
elif page == "About":
    st.header("About the Portal")
    st.write("""This portal is a simple demonstration of how to build an interactive web app using Streamlit. It allows you to create various pages and interact with them via user input.""")
