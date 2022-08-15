# Import initial libraries and dependencies
import sys
import subprocess

# Define function to run pip as a sub-process and install necessary packages
def install():
    subprocess.check_call([
        sys.executable, 
        "-m",
        "pip",
        "install",
        "pandas",
        "prophet",
        "questionary",
        "fire",
        "matplotlib",
        "datetime",
        "alpaca_trade_api",
        "numpy",
        "python-dotenv",
        "pandas_ta"
    ])

# Run program
if __name__ == "__main__":
    install()