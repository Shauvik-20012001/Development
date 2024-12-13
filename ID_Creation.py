import streamlit as st
import pandas as pd

# Function to display login page with "Center" dropdown
def show_login_page():
    st.title("Login Page")
    
    # Username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    # Center dropdown for selection
    center = st.selectbox("Select Center", ["Kolkata", "Indore", "Mysore", "Bhopal", "Ranchi"])
    
    # Employee Type dropdown
    employee_type = st.selectbox("Select Employee Type", ["SLT", "DCS"])

    # Conditional Process dropdown based on Employee Type and Center
    process = st.selectbox("Select Process", ["Collection", "Non_Collection", "Customer Support"])

    # Login button
    if st.button("Login"):
        if username == "admin" and password == "admin":  # Simple login check
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.center = center  # Store selected center in session state
            st.session_state.employee_type = employee_type  # Store selected employee type
            st.session_state.process = process  # Store selected process in session state
            st.session_state.form_displayed = True  # Flag to track whether form is displayed
            st.session_state.data = []  # Initialize the list to hold the form data
        else:
            st.error("Invalid username or password")

# Function to display the form after login
def show_form():
    st.title("Fill the Form")

    # Initialize the data list if it's not already initialized
    if "data" not in st.session_state:
        st.session_state.data = []

    # Display and manage rows
    if st.session_state.center == "Kolkata":
        # Specific form for Kolkata
        emp_id = st.text_input("EMP ID")
        agent_name = st.text_input("Agent Name")
        contact_no = st.text_input("Contact No:")
        official_email = st.text_input("Official Email_ID:")
        department = st.text_input("Department Name:")
        trainer_name = st.text_input("Trainer Name:")
        batch_no = st.text_input("Batch No:")

        # Add Row functionality
        if st.button("Add Row"):
            # Validate inputs and add a new row
            if emp_id and agent_name and contact_no and official_email and department and trainer_name and batch_no:
                new_row = {
                    "EMP ID": emp_id,
                    "Agent Name": agent_name,
                    "Contact No": contact_no,
                    "Official Email_ID": official_email,
                    "Department": department,
                    "Trainer Name": trainer_name,
                    "Batch No": batch_no
                }
                st.session_state.data.append(new_row)
                st.success("Row added successfully!")
                # Clear inputs
                st.experimental_rerun()
            else:
                st.error("Please fill in all fields before adding a row.")

    else:
        # Form for other centers
        emp_id = st.text_input("EMP ID")
        candidate_name = st.text_input("Candidate Name")
        mobile_no = st.text_input("Mobile No.")
        mail_id = st.text_input("Mail ID")
        process_name = st.text_input("Process Name")
        batch_no = st.text_input("Batch No.")
        trainer = st.text_input("Trainer")

        # Add Row functionality
        if st.button("Add Row"):
            # Validate inputs and add a new row
            if emp_id and candidate_name and mobile_no and mail_id and process_name and batch_no and trainer:
                new_row = {
                    "EMP ID": emp_id,
                    "Candidate Name": candidate_name,
                    "Mobile No": mobile_no,
                    "Mail ID": mail_id,
                    "Process Name": process_name,
                    "Batch No": batch_no,
                    "Trainer": trainer
                }
                st.session_state.data.append(new_row)
                st.success("Row added successfully!")
                # Clear inputs
                st.experimental_rerun()
            else:
                st.error("Please fill in all fields before adding a row.")

    # Displaying the table of all added rows
    if st.session_state.data:
        st.write("Your Input Table:")
        df = pd.DataFrame(st.session_state.data)
        st.dataframe(df)

        # Delete Row functionality
        row_to_delete = st.number_input(
            "Enter Row Number to Delete (1-based index):",
            min_value=1,
            max_value=len(df),
            step=1
        )
        if st.button("Delete Row"):
            # Adjust for 1-based index
            if 1 <= row_to_delete <= len(df):
                st.session_state.data.pop(row_to_delete - 1)
                st.success(f"Row {row_to_delete} deleted successfully!")
                st.experimental_rerun()
            else:
                st.error("Invalid row number")

    # Submit button for the form
    if st.button("Submit"):
        if st.session_state.data:
            st.write("Form submitted successfully!")
            # Process the form data here as needed
            st.write(f"Collected Data: {st.session_state.data}")
        else:
            st.error("No rows to submit. Please add some rows first.")

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
