# Import initial libraries and dependencies
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import pandas as pd
import os
import streamlit as st


# Create a function to pull data from Alpaca API and prepare it for use by Prophet
def alpaca_api(tickers, timeframe, start_date, end_date):
    # Load the environment variables from the .env file
    load_dotenv()

    # Set the variables for the Alpaca API key and secret key
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca API REST object
    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version = "V2"
    )

    # Create dataframe using API data
    data_df = alpaca.get_bars(
        tickers,
        timeframe,
        start = start_date,
        end = end_date,
    ).df

    # Drop columns not needed for Prophet usage
    data_df = data_df.drop(["open", "high", "low", "volume", "trade_count", "vwap"], axis=1)

    # Return dataframe for Prophet
    return data_df


def alpaca_api_crypto(tickers, timeframe, start_date, end_date):
    # Load the environment variables from the .env file
    load_dotenv()

    # Set the variables for the Alpaca API key and secret key
    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

    # Create the Alpaca API REST object
    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version = "V2"
    )

    # Create dataframe using API data
    data_df = alpaca.get_crypto_bars(
        tickers,
        timeframe,
        start = start_date,
        end = end_date,
    ).df

    # Filter out all exchanges other than Coinbase and drop redundant exchange column
    data_df = data_df[data_df.exchange == "CBSE"]
    data_df = data_df.drop(axis=1, columns="exchange")

    # Drop columns not needed for Prophet usage
    data_df = data_df.drop(["open", "high", "low", "volume", "trade_count", "vwap"], axis=1)

    # Return dataframe for Prophet
    return data_df