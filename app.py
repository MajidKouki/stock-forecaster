# Import initial libraries and dependencies
import matplotlib
import streamlit as st

# Custom imports - Utilities
from utils.financial_disclaimer import financial_disclaimer
from utils.prophet_forecast import prophet_forecast
from utils.alpaca_api import alpaca_api, alpaca_api_crypto
from utils.crypto_or_stock import crypto_or_stock
from utils.technical_signals import technical_signals

# Custom imports - Data Intake Utilities
from utils.data_intake.timeframe_intake import timeframe_intake
from utils.data_intake.ticker_intake import ticker_intake, ticker_intake_crypto
from utils.data_intake.start_date_intake import start_date_intake
from utils.data_intake.end_date_intake import end_date_intake
from utils.data_intake.prophet_periods import prophet_periods

# Define function to house the program for use with Fire library
def run():
    # Display financial disclaimer before running the rest of the program
    financial_disclaimer()

    # Determine is crypto or stock data will be used with API
    crypto_stock = crypto_or_stock()
    
    # Run either stock or crypto version of ticker intake based on above reply
    if crypto_stock == "Stocks":
        tickers = ticker_intake()
    elif crypto_stock == "Cryptocurrency":
        tickers = ticker_intake_crypto()

    # Intake timeframe data from user and asign it to timeframe while creating frequency and tf
    timeframe, frequency, tf = timeframe_intake()

    # Ask user for forecast length data and use timeframe and tf to ensure program will run without errors
    length = prophet_periods(timeframe, tf)

    # Intake start date from user and assign to start_date
    start_date = start_date_intake()

    # Intake end date from user and assign to end_date
    end_date = end_date_intake()

    if st.button("Run"):

        # Use Alpaca API to create data_df dataframe for Prophet
        if crypto_stock == "Stocks":
            data_df = alpaca_api(tickers, timeframe, start_date, end_date)
        elif crypto_stock == "Cryptocurrency":
            data_df = alpaca_api_crypto(tickers, timeframe, start_date, end_date)

        # Use Prophet to intake data from previous functions and produce a forecast plot and a trend plot
        data_plot, trends_plot = prophet_forecast(data_df, length, frequency)

        # Use Pandas TA to identify buy and sell signals
        signals_plot = technical_signals(data_df)

        # Display plots using streamlit.pyplot
        st.pyplot(data_plot)
        st.pyplot(trends_plot)
        st.pyplot(signals_plot)

# Run the program
if __name__ == "__main__":
    run()