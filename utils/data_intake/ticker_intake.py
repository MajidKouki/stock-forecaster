# Import initial libraries and dependencies
import questionary
import sys

# Create a function that asks user for ticker data for use with Alpaca API. Ensure ticker is formatted properly by converting to upper case
def ticker_intake():
    print("\n")

    tickers = questionary.text("What stock ticker would you like to forecast? Ex. SPY or AAPL").ask()

    # If no ticker is given, sys.exit
    if tickers == "":
        sys.exit("Please try again using a valid ticker.")
    else:
        pass

    # If ticker is given, use .upper() to ensure its properly formatted for API
    tickers = tickers.upper()

    # Return ticker for later use
    return tickers


# Create a function that asks user for ticker data for use with Alpaca API. Ensure ticker is formatted properly by converting to upper case
def ticker_intake_crypto():
    print("\n")

    tickers = questionary.text("What stock ticker would you like to forecast? Ex. BTC or ETH").ask()

    # If no ticker is given, sys.exit
    if tickers == "":
        sys.exit("Please try again using a valid ticker.")
    else:
        pass

    # If ticker is given, use .upper() to ensure its properly formatted for API
    tickers = tickers.upper()

    tickers = tickers + "USD"

    # Return ticker for later use
    return tickers