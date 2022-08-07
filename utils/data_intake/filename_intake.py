# Import initial libraries and dependencies
import questionary

# Create a function that asks user for filename to save charts as
def filename_intake():
    print("\n")
    print("And finally, what would you like the filenames to be? Duplicate names will override old ones and all files will be saved to included 'imgs' folder. Default is 1 & 2.")
    print("\n")

    # USe given name for name variable, else default to 1 & 2
    name = questionary.text("Filename:").ask()

    # Return name for file saving usage
    return name