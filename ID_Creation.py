import streamlit as st
import pandas as pd

# Function to initialize session state for table
def initialize_table():
    if "input_table" not in st.session_state:
        st.session_state["input_table"] = []  # Initialize the table as an empty list

# Function to add a row to the table
def add_row():
    # Collect user input for the new row (You can modify this as needed)
    emp_id = st.text_input("EMP ID", key="emp_id")
    agent_name = st.text_input("Agent Name", key="agent_name")
    contact_no = st.text_input("Contact No", key="contact_no")
    official_email = st.text_input("Official Email_ID", key="official_email")
    department = st.text_input("Department Name", key="department")
    trainer_name = st.text_input("Trainer Name", key="trainer_name")
    batch_no = st.text_input("Batch No", key="batch_no")

    if st.button("Add Row"):
        # Check if all fields are filled
        if not (emp_id and agent_name and contact_no and official_email and department and trainer_name and batch_no):
            st.error("Please fill in all the fields.")
        else:
            # Add the new row to the table
            new_row = {
                "EMP ID": emp_id,
                "Agent Name": agent_name,
                "Contact No": contact_no,
                "Official Email": official_email,
                "Department": department,
                "Trainer Name": trainer_name,
                "Batch No": batch_no
            }
            st.session_state["input_table"].append(new_row)
            st.success("Row added successfully!")
            # Reset the text inputs for the next entry
            st.experimental_rerun()

# Display the table and provide delete functionality
def display_table():
    if st.session_state["input_table"]:
        st.write("Your Input Table:")
        df = pd.DataFrame(st.session_state["input_table"])
        st.dataframe(df)

        # Option to delete a row
        row_to_delete = st.number_input(
            "Enter Row Number to Delete (1-based index):",
            min_value=1,
            max_value=len(df),
            step=1
        )

        if st.button("Delete Row"):
            # Adjust for 1-based index and delete the row
            st.session_state["input_table"].pop(row_to_delete - 1)
            st.success(f"Row {row_to_delete} deleted successfully!")
            # Refresh the table after deletion
            st.experimental_rerun()

# Main function to control the flow
def main():
    # Initialize the table if not already initialized
    initialize_table()

    # Display the form to add a new row
    st.title("Fill the Form and Manage Table")

    # Add Row functionality
    add_row()

    # Display the table and delete row option
    display_table()

if __name__ == "__main__":
    main()
