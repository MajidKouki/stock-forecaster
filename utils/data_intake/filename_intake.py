# Import initial libraries and dependencies
import questionary
import streamlit as st

# Create a function that asks user for filename to save charts as
def filename_intake(tickers, length, tf):
    st.write("Duplicate names will override old ones and all files will be saved to included 'imgs' folder. \nDefault filename is (ticker)(forecast length)(timeframe)1 & 2. Ex. SPY30Days1")

    # USe given name for name variable, else default to 1 & 2
    name = st.text_input("And finally, what would you like the filenames to be?")

    if name == "":
        name = f"{tickers}{length}{tf}"
    else:
        pass

    # Return name for file saving usage
    return name