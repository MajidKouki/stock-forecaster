# Import initial libraries and dependencies
import sys
import streamlit as st

# Create a function that asks user to select either stocks or cryptocurrency to determine API usage
def crypto_or_stock():

    # Ask user to select stocks or cryptocurrency
    crypto_stock = st.selectbox(
        "Would you like to use stock data or cryptocurrency data?",
        ["Stocks", "Cryptocurrency"]
    )

    # Return choice for future usage
    return crypto_stock