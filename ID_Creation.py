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
            if "rows" not in st.session_state:
                st.session_state.rows = []  # Initialize rows if not already initialized
        else:
            st.error("Invalid username or password")

# Function to display the form after login
def show_form():
    st.title("Fill the Form")

    # Check if the selected center is Kolkata
    if st.session_state.center == "Kolkata":
        # Display the dynamic rows for Kolkata
        if "rows" not in st.session_state:
            st.session_state.rows = []

        # Function to add a row of input fields
        def add_row():
            st.session_state.rows.append({
                "emp_id": "",
                "agent_name": "",
                "contact_no": "",
                "official_email": "",
                "department": "",
                "trainer_name": "",
                "batch_no": "",
            })

        # Function to remove the last row
        def remove_row():
            if st.session_state.rows:
                st.session_state.rows.pop()

        # Buttons to add or remove rows
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Add Row"):
                add_row()
        with col2:
            if st.button("Delete Row"):
                remove_row()

        # Display the rows of input fields
        for i, row in enumerate(st.session_state.rows):
            with st.expander(f"Row {i + 1}"):
                row["emp_id"] = st.text_input(f"EMP ID {i + 1}", value=row["emp_id"], key=f"emp_id_{i}")
                row["agent_name"] = st.text_input(f"Agent Name {i + 1}", value=row["agent_name"], key=f"agent_name_{i}")
                row["contact_no"] = st.text_input(f"Contact No. {i + 1}", value=row["contact_no"], key=f"contact_no_{i}")
                row["official_email"] = st.text_input(f"Official Email ID {i + 1}", value=row["official_email"], key=f"official_email_{i}")
                row["department"] = st.text_input(f"Department Name {i + 1}", value=row["department"], key=f"department_{i}")
                row["trainer_name"] = st.text_input(f"Trainer Name {i + 1}", value=row["trainer_name"], key=f"trainer_name_{i}")
                row["batch_no"] = st.text_input(f"Batch No. {i + 1}", value=row["batch_no"], key=f"batch_no_{i}")

        # Submit button for the form
        if st.button("Submit"):
            # Check if all fields are filled for every row
            all_filled = True
            for row in st.session_state.rows:
                if not all(row.values()):
                    all_filled = False
                    break

            if not all_filled:
                st.error("Please fill in all the fields.")
            else:
                # If all fields are filled, proceed with the submission
                st.write("Form submitted successfully!")
                for i, row in enumerate(st.session_state.rows):
                    st.write(f"Row {i + 1}:")
                    st.write(f"EMP ID: {row['emp_id']}")
                    st.write(f"Agent Name: {row['agent_name']}")
                    st.write(f"Contact No.: {row['contact_no']}")
                    st.write(f"Official Email: {row['official_email']}")
                    st.write(f"Department: {row['department']}")
                    st.write(f"Trainer Name: {row['trainer_name']}")
                    st.write(f"Batch No: {row['batch_no']}")

    else:
        # Display the full form for other centers (non-Kolkata)
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
