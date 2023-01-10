import streamlit as st
import pandas as pd
import os
from data import CreateData
import matplotlib.pyplot as plt

# Set the page title
st.title("Expense calculator")

# Add a header
st.header("Welcome to Expense calculator!")

# Add a subheader
st.subheader("Enter your information below to create your Expense calculator")

# Add a text input field for the user's name
names = ['Ajmal','Jouhar']
name = st.selectbox("Select an option:", names,index=1)
options = ["Food", "Entertainment", "Dress"]
selected_option = st.selectbox("Select an option:", options,index=1)

st.write("You selected:", selected_option)
# Add a text input field for the user's email
amount = st.text_input("Amount", "")

# Add a text input field for the user's job title
#job_title = st.text_input("Job Title", "Enter your job title here")

# Add a text area for the user's job description
#job_description = st.text_area("Job Description", "Enter your job description here")

# Add a button to submit the form
proceed = st.button("Add expense")

# Display a success message
if proceed:
   st.success("Thank you for your submission!")

#output
st.markdown(f"Your are logged as **{name}**")

# Create a button that says "Download file"
download_button = st.button("Download file")
if proceed:
   expense1 = pd.read_excel('/app/chatgpt/Expenses.xlsx')
   addNew = CreateData()
   expense2 = addNew.datacreater(name, selected_option, amount)
   expensefinal = pd.concat([expense1, expense2])
   expensefinal.to_excel('Expenses.xlsx', index = False)
expenset = pd.read_excel('/app/chatgpt/Expenses.xlsx')

# Set the file to be downloaded
file = '/app/chatgpt/Expenses.xlsx'


# Only show the file downloader if the button was clicked

if download_button:
    
    st.write("Click the link below to download the file")
    st.markdown("[Download file](" + file + ")")
fig, ax = plt.subplots()
ax.bar(expenset[expenset['Name'] == name]['Category'], expenset[expenset['Name'] == name]['Amount'])
st.pyplot(fig)