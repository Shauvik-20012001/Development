import streamlit as st

# Function to display login page with "Center" dropdown
def show_login_page():
    st.title("Login Page")
    
    # Username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    # Center dropdown for selection
    center = st.selectbox("Select Center", ["Kolkata", "Indore", "Mysore", "Bhopal", "Ranchi"])
    
    # Employee Type dropdown
    Employee_type = st.selectbox("Select Employee Type", ["SLT", "DCS"])

    # Conditional Process dropdown based on Employee Type and Center
    Process = st.selectbox("Select Process", ["Collection", "Non_Collection", "Customer Support"])

    # Login button
    if st.button("Login"):
        if username == "admin" and password == "admin":  # Simple login check
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.center = center  # Store selected center in session state
            st.session_state.employee_type = Employee_type  # Store selected employee type
            st.session_state.process = Process  # Store selected process in session state
            st.session_state.form_displayed = True  # Flag to track whether form is displayed
        else:
            st.error("Invalid username or password")

# Function to display the form after login
def show_form():
    st.title("Fill the Form")



    # Check if the selected center is Kolkata
    if st.session_state.center == "Kolkata":
        # Display only Name and EMP ID fields for Kolkata
        emp_id = st.text_input("EMP ID")
        agent_name = st.text_input("Agent Name")
        contact_no = st.text_input("Contact No:")
        official_email = st.text_input("Official Email_ID:")
        department = st.text_input("Department Name:")
        trainer_name = st.text_input("Trainer Name:")
        batch_no = st.text_input("Batch No :")




        # Submit button for the form
        if st.button("Submit"):
            # Check if both fields are filled
            if not emp_id or not agent_name or not contact_no or not official_email or not department or not trainer_name or not batch_no:
                st.error("Please fill in both fields.")
            else:
                # If both fields are filled, proceed with the submission
                st.write("Form submitted successfully!")
                st.write(f"EMP ID: {emp_id}")
                st.write(f"Agent Name: {agent_name}")
                st.write(f"Contact No: {contact_no}")
                st.write(f"Official Email: {official_email}")
                st.write(f"Department: {department}")
                st.write(f"Trainer Name: {trainer_name}")
                st.write(f"Batch No: {batch_no}")


    else:
        # Display the full form for other centers
        emp_id = st.text_input("EMP ID")
        candidate_name = st.text_input("Candidate Name")
        mobile_no = st.text_input("Mobile No.")
        mail_id = st.text_input("Mail ID")
        process_name = st.text_input("Process Name")
        batch_no = st.text_input("Batch No.")
        trainer = st.text_input("Trainer")

        # Submit button for the form
        if st.button("Submit"):
            # Check if all fields are filled
            if not emp_id or not candidate_name or not mobile_no or not mail_id or not process_name or not batch_no or not trainer:
                st.error("Please fill in all the fields.")
            else:
                # If all fields are filled, proceed with the submission
                st.write("Form submitted successfully!")
                # You can process and save form data here
                st.write(f"EMP ID: {emp_id}")
                st.write(f"Candidate Name: {candidate_name}")
                st.write(f"Mobile No.: {mobile_no}")
                st.write(f"Mail ID: {mail_id}")
                st.write(f"Process Name: {process_name}")
                st.write(f"Batch No.: {batch_no}")
                st.write(f"Trainer: {trainer}")

# Main function to control the flow of the app
def main():
    # Initialize session state if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.form_displayed = False  # Ensure form is not displayed by default

    if not st.session_state.logged_in:
        show_login_page()  # Show login page if not logged in
    else:
        show_form()  # Show the form after login

if __name__ == "__main__":
    main()
