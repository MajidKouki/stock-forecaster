# Import initial libraries and dependencies
from datetime import date
import questionary
import pandas as pd

# Create a function that asks user for data end date and defaults to the current date if nothing is given
def end_date_intake():
    print("\n")

    # Ask user to input a date using required format
    end = questionary.text("Enter the end date using following format:'1234-56-78.' Default is current date.").ask()

    # If nothing is entered, use default date
    if end == "":
        end = str(date.today())
        print(f"Default Date: {end}")
    else:
        print(f"Selected Date: {end}")

    # Ensure end date is formatted correctly for Alpaca API
    end_date = pd.Timestamp(end, tz="America/New_York").isoformat()

    # Return end date for Alpaca API
    return end_date