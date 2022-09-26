# Import initial libraries and dependencies
import questionary
import sys
import streamlit as st

# Create a function that asks user to select from a list of three timeframes for usage with Alpaca API and Prophet
def timeframe_intake():


    # Ask user to select one of three timeframes
    timeframe = st.selectbox(
        "Which timeframe would you like to use?",
        ["1Day", "1Hour", "1Min"]
    )

    # Use a loop to set tf and frequency based on selected timeframe. Error message included just in case
    if timeframe == "1Day":
        frequency = "D"
        tf = "Days"
    elif timeframe == "1Hour":
        frequency = "H"
        tf = "Hours"
    elif timeframe == "1Min":
        frequency = "M"
        tf = "Minutes"
    else:
        sys.exit("An error has occured. Please try again.")

    # Return timeframe, frequency, and tf for later use
    return timeframe, frequency, tf