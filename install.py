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
        "matplotlib",
        "pandas_ta",
        "streamlit",
        "datetime",
        "prophet",
        "pandas",
        "numpy",
        "yfinance"
    ])

# Run program
if __name__ == "__main__":
    install()