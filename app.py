# Import initial libraries and dependencies
import matplotlib
import streamlit as st

# Custom imports - Utilities
from utils.prophet_forecast import prophet_forecast
from utils.crypto_or_stock import crypto_or_stock
from utils.yahoo_api import yahoo_api

# Custom imports - Data Intake Utilities
from utils.data_intake.timeframe_intake import timeframe_intake
from utils.data_intake.ticker_intake import ticker_intake, ticker_intake_crypto
from utils.data_intake.prophet_periods import prophet_periods
from utils.data_intake.interval_intake import interval_intake
from utils.data_intake.period_intake import period_intake

# Define function to house the program
def run():
    with st.sidebar:
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

        # Intake period from user and assign to period
        period = period_intake()

        # Intake interval from user and assign to interval
        interval = interval_intake()

        # Create a variable to determine whether plots are displayed or not
        ran = False

        if st.button("Run"):
            with st.spinner("Loading..."):

                # Use the yahoo finance api to get ticker data using provided information
                data_df = yahoo_api(tickers, period, interval)

                # Check if the data_df dataframe is empty and return a warning else run the appropriate code
                if data_df.empty:
                    st.warning("Invalid Ticker! Please try again.")
                else:
                    # Switch ran to True to show plots
                    ran = True

                    # Use Prophet to intake data from previous functions and produce a forecast plot and a trend plot
                    data_plot, trends_plot = prophet_forecast(data_df, length, frequency)

        # Create blank space for spacing purposes
        st.markdown("#")

    # # Display plots using streamlit.pyplot if run button has been pressed else display a message
    if ran is True:
        st.pyplot(data_plot, dpi=500)
        st.pyplot(trends_plot, dpi=500)
    else:
        st.markdown("#### Fill in the details in the sidebar and hit Run to get started!")

# Run the program
if __name__ == "__main__":
    run()