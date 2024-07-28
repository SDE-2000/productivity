import streamlit as st

def page1():
    st.title("Page 1")

    associate_id = st.text_input("Associate ID")
    associate_name = st.text_input("Associate Name")
    date = st.date_input("Date")

    col1, col2 = st.columns([2, 1])  # Adjust column widths as needed

    with col1:
        submit_button = st.button("Submit", disabled=not (associate_id and associate_name and date))
        if submit_button:
            st.session_state.page = "page2"
            st.session_state.data = {
                "associate_id": associate_id,
                "associate_name": associate_name,
                "date": date
            }
    with col2:
        get_data_button = st.button("Get Data", disabled=not (associate_id and associate_name and date))
        if get_data_button:
            # Implement your data retrieval logic here
            st.write("Fetching data...")  # Placeholder message


def page2():
    st.title("productivity")

    data = st.session_state.data
    st.write(f"Associate ID: {data['associate_id']}")
    st.write(f"Associate Name: {data['associate_name']}")
    st.write(f"Date: {data['date']}")

    # Additional form fields
    tower = st.text_input("Tower")
    service_line = st.text_input("Service Line")
    project_id = st.text_input("Project ID")
    project_name = st.text_input("Project Name")
    line_name = st.text_input("Line Name")
    total_worked_hour = st.number_input("Total Worked Hour", min_value=0.0)
    hours_test_design = st.number_input("No of hours worked in test design", min_value=0.0)
    hours_test_data_prep = st.number_input("No of hours worked in test data preparation", min_value=0.0)
    hours_test_execution = st.number_input("No of hours worked in test execution", min_value=0.0)
    no_of_test_case_designed = st.number_input("No of Test case designed", min_value=0)
    no_of_test_data_prepared = st.number_input("No of Test data prepared", min_value=0)
    no_of_test_execution = st.number_input("No of Test execution", min_value=0)
    no_of_story_card_tested = st.number_input("No of story card tested", min_value=0)
    card_no = st.text_input("Card No")
    story_points = st.number_input("Story points", min_value=0)
    challenges = st.text_area("Challenges")
    impact_hours = st.number_input("Impact Hours", min_value=0.0)
    comment = st.text_area("Comment")

    # Calculated fields (logic improved)
    total_hours_breakdown = hours_test_design + hours_test_data_prep + hours_test_execution
    if total_hours_breakdown > 0:  # Avoid division by zero
        design_productivity = (no_of_test_case_designed / hours_test_design) * total_worked_hour
        data_prep_productivity = (no_of_test_data_prepared / hours_test_data_prep) * total_worked_hour
        execution_productivity = (no_of_test_execution / hours_test_execution) * total_worked_hour
    else:
        design_productivity, data_prep_productivity, execution_productivity = 0.0, 0.0, 0.0

    # Display calculated fields
    st.write(f"Design Productivity: {design_productivity:.2f}")
    st.write(f"Data Prep Productivity: {data_prep_productivity:.2f}")
    st.write(f"Execution Productivity: {execution_productivity:.2f}")

    # Save records to database (you'll need to implement this logic)
    if st.button("Submit"):
        # Save the entered data and calculated fields to your database
        # Implement your database interaction here
        st.write("Records saved successfully!")  # Placeholder message

def main():
    if "page" not in st.session_state:
        st.session_state.page = "page1"

    if st.session_state.page == "page1":
        page1()
    elif st.session_state.page == "page2":
        page2()

if __name__ == "__main__":
    main()
