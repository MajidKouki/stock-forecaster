# Import initial libraries and dependencies
import sys
import subprocess

# Implement pip as a sub-process and install necessary packages
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
    "dotenv"
])