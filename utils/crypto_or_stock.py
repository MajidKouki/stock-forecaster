# Import initial libraries and dependencies
import questionary
import sys


# Create a function that asks user to select either stocks or cryptocurrency to determine API usage
def crypto_or_stock():
    print("\n")

    # Ask user to select stocks or cryptocurrency
    crypto_stock = questionary.select(
        "Would you like to use stock data or cryptocurrency data?",
        choices=["Stocks", "Cryptocurrency"]
    ).ask()

    # Return choice for future usage
    return crypto_stock