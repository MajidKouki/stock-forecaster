# Import initial libraries and dependencies
import pandas as pd
import streamlit as st

# Create a function that asks user for data start date and defaults to the start of 2020 if nothing is given
def period_intake():

    # Ask user to input a date using required format
    period = st.text_input("Enter the period ex. 12mo.")

    # If nothing is entered, use default date
    if period == "":
        period = "12mo"
        print(f"{period}")
    else:
        print(f"{period}")

    # Return start date for Alpaca API
    return period

# m, h, d, wk, mo