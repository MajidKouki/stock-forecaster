# Import initial libraries and dependencies
import questionary

# Create a function that asks user for filename to save charts as
def filename_intake(tickers, length, tf):
    print("\n")
    print("Duplicate names will override old ones and all files will be saved to included 'imgs' folder. \nDefault filename is (ticker)(forecast length)(timeframe)1 & 2. Ex. SPY30Days1")
    print("\n")

    # USe given name for name variable, else default to 1 & 2
    name = questionary.text("And finally, what would you like the filenames to be?").ask()

    if name == "":
        name = f"{tickers}{length}{tf}"
    else:
        pass

    # Return name for file saving usage
    return name