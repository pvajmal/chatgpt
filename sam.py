import streamlit as st
import pandas as pd
import os
from data import CreateData

# Set the page title
st.title("Expense calculator")

# Add a header
st.header("Welcome to Expense calculator!")

# Add a subheader
st.subheader("Enter your information below to create your Expense calculator")

# Add a text input field for the user's name
name = st.text_input("Name", "Enter your name here")
options = ["Food", "Entertainment", "Dress"]
selected_option = st.selectbox("Select an option:", options,index=1)

st.write("You selected:", selected_option)
# Add a text input field for the user's email
amount = st.text_input("Amount", "Enter amount here")

# Add a text input field for the user's job title
#job_title = st.text_input("Job Title", "Enter your job title here")

# Add a text area for the user's job description
#job_description = st.text_area("Job Description", "Enter your job description here")

# Add a button to submit the form
proceed = st.button("Add expense")

# Display a success message
st.success("Thank you for your submission!")

#output
st.markdown(f"Your name is **{proceed}**")

# Create a button that says "Download file"
download_button = st.button("Download file")
if proceed:
   expense1 = pd.read_excel('/app/chatgpt/Expenses.xlsx')
   addNew = CreateData()
   expense2 = addNew.datacreater(name, selected_option, amount)
   expensefinal = pd.concat([expense1, expense2])
   expensefinal.to_xlsx('Expenses.xlsx', index = False)
expense1 = pd.read_excel('/app/chatgpt/Expenses.xlsx')
st.markdown(f"Your name is **{expense1.shape[1]}**")
# Set the file to be downloaded
file = '/app/chatgpt/Expenses.xlsx'

'''with open(file) as f:
   st.download_button(file, f)  # Defaults to "text/plain"'''

# Only show the file downloader if the button was clicked
if download_button:
    st.markdown('Exporting current data to Excel...')
    st.download("/app/chatgpt/Expenses.xlsx")
    st.markdown('Done!')