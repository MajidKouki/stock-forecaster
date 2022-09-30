# Import initial libraries and dependencies
import matplotlib
import streamlit as st

# Custom imports - Utilities
from utils.prophet_forecast import prophet_forecast
from utils.alpaca_api import alpaca_api, alpaca_api_crypto
from utils.crypto_or_stock import crypto_or_stock
# from utils.technical_signals import technical_signals

# Custom imports - Data Intake Utilities
from utils.data_intake.timeframe_intake import timeframe_intake
from utils.data_intake.ticker_intake import ticker_intake, ticker_intake_crypto
from utils.data_intake.start_date_intake import start_date_intake
from utils.data_intake.end_date_intake import end_date_intake
from utils.data_intake.prophet_periods import prophet_periods

# Define function to house the program for use with Fire library
def run():
    # Use streamlit markdown to decorate the web interface
    st.markdown("# Stock Forecaster")

    # Display a financial disclaimer
    st.write("By using this application, you acknowledge that this is NOT financial advice and is merely a tool. \nThe creator of this program is not liable for any negative consequences that may occur from using it or the data it provides. \nContinue at your own risk.")
    

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

    # 
    st.write("Running the program will forecast the chosen ticker for the specified period as well as a trend chart.")

    if st.button("Run"):

        # Use Alpaca API to create data_df dataframe for Prophet
        if crypto_stock == "Stocks":
            data_df = alpaca_api(tickers, timeframe, start_date, end_date)
        elif crypto_stock == "Cryptocurrency":
            data_df = alpaca_api_crypto(tickers, timeframe, start_date, end_date)

        # Use Prophet to intake data from previous functions and produce a forecast plot and a trend plot
        data_plot, trends_plot = prophet_forecast(data_df, length, frequency)

        # Use Pandas TA to identify buy and sell signals
        # signals_plot = technical_signals(data_df)

        # Display plots using streamlit.pyplot
        st.pyplot(data_plot, dpi=500)
        st.pyplot(trends_plot, dpi=500)
        # st.pyplot(signals_plot, dpi=500)

# Run the program
if __name__ == "__main__":
    run()