# Import initial libraries and dependencies
import fire
import matplotlib

# Custom imports - Utilities
from utils.financial_disclaimer import financial_disclaimer
from utils.prophet_forecast import prophet_forecast
from utils.alpaca_api import alpaca_api, alpaca_api_crypto
from utils.crypto_or_stock import crypto_or_stock
# Custom imports - Data Intake Utilities
from utils.data_intake.timeframe_intake import timeframe_intake
from utils.data_intake.ticker_intake import ticker_intake, ticker_intake_crypto
from utils.data_intake.start_date_intake import start_date_intake
from utils.data_intake.end_date_intake import end_date_intake
from utils.data_intake.filename_intake import filename_intake
from utils.data_intake.prophet_periods import prophet_periods


# Forecast code using Alpaca get_bars for stock data
def stock_forecast():
    # Intake ticker data from user and assign to tickers
    tickers = ticker_intake()

    # Intake timeframe data from user and asign it to timeframe while creating frequency and tf
    timeframe, frequency, tf = timeframe_intake()

    # Ask user for forecast length data and use timeframe and tf to ensure program will run without errors
    length = prophet_periods(timeframe, tf)

    # Intake start date from user and assign to start_date
    start_date = start_date_intake()

    # Intake end date from user and assign to end_date
    end_date = end_date_intake()

    # Intake filename data from user and assign to name
    name = filename_intake(tickers, length, tf)

    # Use Alpaca API to create data_df dataframe for Prophet
    data_df = alpaca_api(tickers, timeframe, start_date, end_date)

    # Use Prophet to intake data from previous functions and produce a forecast plot and a trend plot
    data_plot, trends_plot = prophet_forecast(data_df, length, frequency)

    # Save Prophet plots to 'imgs' folder using chosen filenames
    data_plot.savefig(f"./imgs/{name}Forecast.png")
    trends_plot.savefig(f"./imgs/{name}Trends.png")
    # indicator_plot.savefig(f"./imgs/{name}Indicators.png")


# Forecast code using Alpaca get_crypto_bars for crypto data
def crypto_forecast():
    # Intake ticker data from user and assign to tickers
    tickers = ticker_intake_crypto()

    # Intake timeframe data from user and asign it to timeframe while creating frequency and tf
    timeframe, frequency, tf = timeframe_intake()

    # Ask user for forecast length data and use timeframe and tf to ensure program will run without errors
    length = prophet_periods(timeframe, tf)

    # Intake start date from user and assign to start_date
    start_date = start_date_intake()

    # Intake end date from user and assign to end_date
    end_date = end_date_intake()

    # Intake filename data from user and assign to name
    name = filename_intake(tickers, length, tf)

    # Use Alpaca API to create data_df dataframe for Prophet
    data_df = alpaca_api_crypto(tickers, timeframe, start_date, end_date)

    # Use Prophet to intake data from previous functions and produce a forecast plot and a trend plot
    data_plot, trends_plot = prophet_forecast(data_df, length, frequency)

    # Save Prophet plots to 'imgs' folder using chosen filenames
    data_plot.savefig(f"./imgs/{name}Forecast.png")
    trends_plot.savefig(f"./imgs/{name}Trends.png")
    # indicator_plot.savefig(f"./imgs/{name}Indicators.png")


# Define function to house the program for use with Fire library
def run():
    # Display financial disclaimer before running the rest of the program
    financial_disclaimer()

    # Determine is crypto or stock data will be used with API
    crypto_stock = crypto_or_stock()
    
    # Run stock version of code or crypto version of code based on answer above
    if crypto_stock == "Stocks":
        stock_forecast()
    elif crypto_stock == "Cryptocurrency":
        crypto_forecast()

# Run the program
if __name__ == "__main__":
    fire.Fire(run)