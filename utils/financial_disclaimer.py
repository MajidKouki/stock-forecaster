# Import initial libraries and dependencies
import streamlit as st

# Create a function that displays a financial disclaimer when the program is run and requires user to agree before proceeding
def financial_disclaimer():
    st.write("By using this application, you acknowledge that this is NOT financial advice and is merely a tool. \nThe creator of this program is not liable for any negative consequences that may occur from using it or the data it provides. \nContinue at your own risk.")