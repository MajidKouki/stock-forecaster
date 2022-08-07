# Import initial libraries and dependencies
import questionary
import sys

# Create a function that displays a financial disclaimer when the program is run and requires user to agree before proceeding
def financial_disclaimer():
    print("By using this application, you acknowledge that this is NOT financial advice and is merely a tool. \nThe creator of this program is not liable for any negative consequences that may occur from using it or the data it provides. \nContinue at your own risk.")
    print("\n")

    # If user agrees, proceed. If user does not agree, sys.exit
    disclaimer = questionary.confirm("Do you agree to the above terms?").ask()
    
    if disclaimer == True:
        pass
    else:
        sys.exit("Sorry, you must agree to the above disclaimer in order to use this program.")