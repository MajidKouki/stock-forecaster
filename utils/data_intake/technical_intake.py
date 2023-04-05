# Import initial libraries and dependencies
import streamlit as st
import pandas_ta as ta


# Define a function to intake indicators for use in technical_signals
def technical_intake():
    indicator_1 = st.selectbox(
        "Select the first indicator",
        ["EMA"]
    )

    indicator_2 = st.selectbox(
        "Select the second indicator",
        ["EMA"]
    )

    return indicator_1, indicator_2