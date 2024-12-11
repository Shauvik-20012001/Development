import streamlit as st

# Function to display login page
def show_login_page():
    st.title("Login Page")
    
    # Username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    # Login button
    if st.button("Login"):
        if username == "admin" and password == "admin":  # Simple login check
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.center = None  # Reset center and type on new login
            st.session_state.center_type = None
            st.session_state.form_displayed = False  # Flag to track whether form is displayed
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to display center selection and center type options
def show_center_selection_page():
    st.title("Select Center and Type")

    # Dropdown for selecting the center
    center = st.selectbox("Select Center", ["Kolkata", "Indore", "Mysore", "Bhopal", "Ranchi"])
    st.session_state.center = center  # Store selected center in session state
    
    # Show different radio buttons based on selected center
    if center == 'Kolkata':
        center_type = st.radio("Select Type", ["Collection", "Non-Collection", "Customer Support"])
    else:
        center_type = st.radio("Select Type", ["Collection", "Non-Collection"])
    
    st.session_state.center_type = center_type  # Store selected center type in session state

    # Submit button for center and type selection
    if st.button("Submit"):
        st.session_state.form_displayed = True  # Flag to show the form fields
        st.experimental_rerun()

# Function to display the additional form fields after center and type selection
def show_form():
    st.title("Fill the Form")

    # Based on the center, display different input fields
    if st.session_state.center == 'Kolkata':
        st.text_input("EMP ID")
        st.text_input("Agent Name")
        st.text_input("Contact No.")
        st.text_input("Official E Mail Id")
        st.text_input("Process Name")
        st.text_input("Trainer Name")
        st.text_input("Batch No.")
    else:
        st.text_input("EMP ID")
        st.text_input("Candidate Name")
        st.text_input("Mobile No")
        st.text_input("Mail ID")
        st.text_input("Process Name")
        st.text_input("Batch No.")
        st.text_input("Trainer")

# Main function to control the flow of the app
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.form_displayed = False  # Track if the form is displayed
        st.session_state.center = None
        st.session_state.center_type = None
    
    if not st.session_state.logged_in:
        show_login_page()
    elif not st.session_state.form_displayed:
        show_center_selection_page()  # Display center and type selection
    else:
        show_form()  # Display the form fields after submission

if __name__ == "__main__":
    main()
