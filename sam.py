import streamlit as st
import pandas as pd
import os

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
st.markdown(f"Your name is **{os.getcwd(), os.listdir()}**")

# Create a button that says "Download file"
download_button = st.button("Download file")

df = pd.DataFrame()

df.to_csv('aju.csv')
# Set the file to be downloaded
file = '/app/chatgpt/data.csv'

# Create the file downloader
st.download(file, caption="Download file")

# Only show the file downloader if the button was clicked
if download_button:
    st.markdown("Click the button to download the file.")