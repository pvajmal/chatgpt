import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import seaborn as sns

# Set the page config and include CSS
st.set_page_config(page_title="Expense Calculator", page_icon=":moneybag:", layout="wide")
st.markdown("<link rel='stylesheet' type='text/css' href='style.css'>", unsafe_allow_html=True)

# Add a header
st.header("Welcome to Expense calculator!")
st.subheader("Enter your information below to add your Expense")

# Add date picker
date_expense = st.date_input("Enter the date of expense")

# Add options for user name and expense category
names = ['Ajmal','Jouhar']
name = st.selectbox("Select User:", names,index=1)
options = ["Food", "Entertainment", "Dress"]
selected_option = st.selectbox("Select an option:", options,index=1)

# Add input fields for amount and description
amount = st.number_input("Amount", value=0, step=10)
description = st.text_input("Description", "")

# Add image
#st.image('logo.png')

# Add Sidebar
st.sidebar.header("Filter by")
filter_by_name = st.sidebar.checkbox("Name")
filter_by_date = st.sidebar.checkbox("Date")

# Add button to submit form
if st.button("Add expense"):
    expense1 = pd.read_excel('Expenses.xlsx')
    expense2 = pd.DataFrame({'Name': name, 'Category': selected_option, 'Amount': amount, 'Description': description, 'Date': date_expense}, index=[0])
    expensefinal = pd.concat([expense1,expense2], axis = 0)
    expensefinal.to_excel('/app/chatgpt/Expenses.xlsx', index = False)

if filter_by_name or filter_by_date:
    expensefinal = pd.read_excel('/app/chatgpt/Expenses.xlsx')
    expensefinal['Date'] = pd.to_datetime(expensefinal['Date'])
    if filter_by_name:
        expensefinal = expensefinal[expensefinal['Name'] == name]
    if filter_by_date:
        expensefinal = expensefinal[expensefinal['Date'].dt.date == date_expense]
    st.dataframe(expensefinal)   
    if st.checkbox('Show Graph'):
        fig, ax = plt.subplots()
        expname = expensefinal.groupby('Category')['Amount'].sum().reset_index()
        ax.bar(expname.iloc[:,0], expname.iloc[:,1])
        ax.set_title("Expenses by category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Expense amount")

        plt.style.use("ggplot")
        st.pyplot(fig)

