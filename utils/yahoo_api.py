# Import initial libraries and dependencies
import pandas as pd
import yfinance as yf
import streamlit as st

# Create a function to pull data from Yahoo Finance API and prepare it for use by Prophet
def yahoo_api(tickers, period, interval):
    # Create dataframe using API data
    data_df = yf.download(
        tickers = tickers, 
        period = period, 
        interval = interval
    )

    # Drop columns not needed for Prophet usage
    data_df = data_df.drop(["Open", "High", "Low", "Adj Close", "Volume"], axis=1)

    # Return dataframe for Prophet
    return data_df