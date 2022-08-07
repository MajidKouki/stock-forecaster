# Import initial libraries and dependencies
import questionary
import sys

# Create a function that asks the user how long they want to forecast into the future for use with Prophet
def prophet_periods(timeframe, tf):
    print("\n")
    print("The selected length will also determine how long the model takes to run. Keep that in mind when choosing.")
    print("When entering a forecast amount, use only whole numbers and remember your timeframe choice. 1 day ex. 1Day = 1, 1Hour = 24, 1Min = 1440. Defaults are 30, 720, and 1440.")
    print("\n")

    # Ask for user input for forecasting
    length = questionary.text("How long do you want to forecast?").ask()

    # Loop through length variable and timeframe to assign default values if needed
    if length == "" and timeframe == "1Day":
        length = 30
    elif length == "" and timeframe == "1Hour":
        length = 720
    elif length == "" and timeframe == "1Min":
        length = 1440
    else:
        pass

    # Ensure length variable is an integer to prevent Prophet errors
    length = int(length)

    # Show chosen length and unit of measure
    print(f"Forecasting {length} {tf}")

    # Return length for use with Prophet
    return length