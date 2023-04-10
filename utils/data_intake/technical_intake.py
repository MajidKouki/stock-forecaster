# Import initial libraries and dependencies
import streamlit as st
import pandas_ta as ta


# Define a function to intake indicators for use in technical_signals
def technical_intake():
    # Prompt used to choose between available indicators
    indicator_1 = st.selectbox(
        "Select the first indicator",
        ["EMA", "SMA"]
    )
    indicator_2 = st.selectbox(
        "Select the second indicator",
        ["EMA", "SMA"]
    )  

    # Intake the length for the indicators and assign a default value if needed
    indicator_1_len = st.text_input("Enter the length for the first indicator")
    if indicator_1_len == "":
        indicator_1_len = 14
    
    indicator_2_len = st.text_input("Enter the length for the second indicator")
    if indicator_2_len == "":
        indicator_2_len = 28

    # Ensure indicators are integers
    indicator_1_len = float(indicator_1_len)
    indicator_2_len = float(indicator_2_len)

    # Return indicator info for use in charting
    return indicator_1, indicator_2, indicator_1_len, indicator_2_len