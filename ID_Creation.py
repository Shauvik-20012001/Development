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
            if "rows" not in st.session_state:
                st.session_state.rows = []  # Initialize rows in session state
        else:
            st.error("Invalid username or password")

# Function to display the form after login
def show_form():
    st.title("Fill the Form")

    # Check if the selected center is Kolkata
    if st.session_state.center == "Kolkata":
        # Display the form fields for Kolkata (Name, EMP ID, etc.)
        if "rows" not in st.session_state:
            st.session_state.rows = []

        # Add button for adding rows
        if st.button("Add Row"):
            # Add a new row (dict to store values)
            st.session_state.rows.append({
                "emp_id": "",
                "agent_name": "",
                "contact_no": "",
                "official_email": "",
                "department": "",
                "trainer_name": "",
                "batch_no": ""
            })

        # Display rows
        for i, row in enumerate(st.session_state.rows):
            col1, col2, col3 = st.columns(3)
            with col1:
                row["emp_id"] = st.text_input(f"EMP ID {i+1}", value=row["emp_id"], key=f"emp_id_{i}")
            with col2:
                row["agent_name"] = st.text_input(f"Agent Name {i+1}", value=row["agent_name"], key=f"agent_name_{i}")
            with col3:
                row["contact_no"] = st.text_input(f"Contact No. {i+1}", value=row["contact_no"], key=f"contact_no_{i}")

            # Delete button for each row
            delete_button = st.button(f"Delete Row {i+1}", key=f"delete_{i}")
            if delete_button:
                del st.session_state.rows[i]
                st.experimental_rerun()  # Rerun to update the rows after deletion

        # Submit button for the form
        if st.button("Submit"):
            # Check if all rows have all fields filled
            all_fields_filled = True
            for row in st.session_state.rows:
                if not row["emp_id"] or not row["agent_name"] or not row["contact_no"] or not row["official_email"] or not row["department"] or not row["trainer_name"] or not row["batch_no"]:
                    all_fields_filled = False
                    break

            if all_fields_filled:
                st.write("Form submitted successfully!")
                for row in st.session_state.rows:
                    st.write(f"EMP ID: {row['emp_id']}, Agent Name: {row['agent_name']}, Contact No: {row['contact_no']}, Official Email: {row['official_email']}, Department: {row['department']}, Trainer: {row['trainer_name']}, Batch No: {row['batch_no']}")
            else:
                st.error("Please fill in all the fields.")

    else:
        # Full form for other centers
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
