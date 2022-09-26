# Import initial libraries and dependencies
import questionary
import pandas as pd
import streamlit as st

# Create a function that asks user for data start date and defaults to the start of 2020 if nothing is given
def start_date_intake():

    # Ask user to input a date using required format
    start = st.text_input("Enter the start date using following format:'1234-56-78.' Default is start of 2018.")

    # If nothing is entered, use default date
    if start == "":
        start = "2020-01-01"
        print(f"Default Date: {start}")
    else:
        print(f"Selected Date: {start}")

    # Ensure start date is formatted correctly for Alpaca API
    start_date = pd.Timestamp(start, tz="America/New_York").isoformat()

    # Return start date for Alpaca API
    return start_date