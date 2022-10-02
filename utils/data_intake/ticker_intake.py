# Import initial libraries and dependencies
import sys
import streamlit as st

# Create a function that asks user for ticker data for use with Alpaca API. Ensure ticker is formatted properly by converting to upper case
def ticker_intake():

    tickers = st.text_input("Stock Ticker:", placeholder="SPY")

    # If ticker is given, use .upper() to ensure its properly formatted for API
    tickers = tickers.upper()

    # Return ticker for later use
    return tickers


# Create a function that asks user for ticker data for use with Alpaca API. Ensure ticker is formatted properly by converting to upper case
def ticker_intake_crypto():

    tickers = st.text_input("Coin Ticker:", placeholder="BTC")

    # If ticker is given, use .upper() to ensure its properly formatted for API
    tickers = tickers.upper()

    tickers = tickers + "USD"

    # Return ticker for later use
    return tickers