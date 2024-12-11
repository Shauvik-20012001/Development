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
            st.session_state.logged_in = True  # Mark logged-in state
            st.session_state.username = username  # Save username in session state
            st.session_state.page = "center_selection"  # Redirect to center selection page
        else:
            st.error("Invalid username or password")

# Function to display center selection page
def show_center_page():
    st.title("Select Center")

    # Dropdown for selecting the center
    center = st.selectbox("Select Center", ["Kolkata", "Indore", "Mysore", "Bhopal", "Ranchi"])

    # Show different radio buttons based on selected center
    if center == 'Kolkata':
        center_type = st.radio("Select Type", ["Collection", "Non-Collection", "Customer Support"])
    else:
        center_type = st.radio("Select Type", ["Collection", "Non-Collection"])
    
    # Submit button
    if st.button("Submit"):
        st.write(f"Center: {center}, Type: {center_type}")
        # Here, you can add further logic to handle form submission

# Main function to control the flow of the app
def main():
    # Initialize session states if not already set
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "page" not in st.session_state:
        st.session_state.page = "login"  # Default to the login page
    
    # Check the page state and show the corresponding page
    if st.session_state.page == "login":
        show_login_page()
    elif st.session_state.page == "center_selection":
        show_center_page()

if __name__ == "__main__":
    main()
