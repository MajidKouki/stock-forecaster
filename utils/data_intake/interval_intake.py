# Import initial libraries and dependencies
import pandas as pd
import streamlit as st

# Create a function that asks user for data start date and defaults to the start of 2020 if nothing is given
def interval_intake():

    # Ask user to input a date using required format
    interval = st.text_input("Enter the interval ex. 1d.")

    # If nothing is entered, use default date
    if interval == "":
        interval = "1d"
        print(f"{interval}")
    else:
        print(f"{interval}")

    # Return start date for Alpaca API
    return interval

# m, h, d, wk, mo