import streamlit as st

# Set the page title
st.title("Resume Builder")

# Add a header
st.header("Welcome to the resume builder!")

# Add a subheader
st.subheader("Enter your information below to create your resume.")

# Add a text input field for the user's name
name = st.text_input("Name", "Enter your name here")

# Add a text input field for the user's email
email = st.text_input("Email", "Enter your email here")

# Add a text input field for the user's job title
job_title = st.text_input("Job Title", "Enter your job title here")

# Add a text area for the user's job description
job_description = st.text_area("Job Description", "Enter your job description here")

# Add a button to submit the form
st.button("Create Resume")

# Display a success message
st.success("Thank you for creating your resume!")

#output
st.markdown(f"Your name is **{name}**")