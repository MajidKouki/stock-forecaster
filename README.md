# Stock Forecasting CLI

Simple CLI application using Prophet library and Alpaca API to provide stock forecasts and trend data. This application was designed for a client with the intention of creating a very simple to use system for non-technical users with minimal setup and detailed instructions while enabling easy access to machine learning tools for time series forecasting and trend analysis.

---

## Technologies

This project leverages python with the following packages:

* [Pandas](https://github.com/pandas-dev/pandas) - For plotting and dataframes.

* [Dotenv](https://pypi.org/project/python-dotenv/) - For accessing the .env file.

* [Prophet](https://github.com/facebook/prophet) - For forecasting.

* [Alpaca Trade API](https://github.com/alpacahq/alpaca-trade-api-python) - For financial data from [Alpaca](https://alpaca.markets)

* [Fire](https://github.com/google/python-fire) - For the command line interface and entry-point.

* [Questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs.

* [Matplotlib](https://github.com/matplotlib/matplotlib) - For plotting.

* [Numpy](https://github.com/numpy/numpy) - For Prophet usage.

* [Pandas TA](https://github.com/twopirllc/pandas-ta) - For indicators.

---

## Installation Guide

This project assumes the user has basics setup (git, terminal or git bash, python). If not, please refer to appropriate websites and documentation prior to using this project.

Before first running the application, it may be necessary to install the required dependencies. This can be done using traditional pip installation or the included install file (recommended).

To install using the install file, navigate to the project directory and run the following code:

```
python install.py install
```

This will run a subprocess to install all the dependencies in a single command. Alternatively, manual installation can be done as follows:

```
pip install pandas, prophet, questionary, fire, matplotlib, datetime, numpy, prophet, python-dotenv, alpaca-trade-api, pandas_ta
```

Next it will be necessary to populate a .env file with the necessary Alpaca API keys. Signing up with Alpaca is easy and allows future usage with data and trading APIs. An example.env file is included and can be used to store API data as long as it's properly renamed. Example of the .env:

```
ALPACA_API_KEY = "<Your API Key Here>"
ALPACA_SECRET_KEY = "<Your Secret Key Here>"
```

Once the API keys have been generated on the Alpaca website and the example.env has been populated, run the following command to properly rename:

```
mv example.env .env 
```

---

## Usage

After the initial setup and install, the program can be run by typing the following into the terminal:

```
python app.py
```

As the program is opened, a financial disclaimer will appear to ensure the user is aware any risks that may arise from following the advice given by the software. After agreeing to it, the program takes the following user data:

* Stock or Crypto data
* Stock Ticker - ex. SPY or BTC
* Timeframe - Either 1Day, 1Hour or 1Min
* Forecast Length - Defaults are 30 days, 720 hours, or 1440 minutes
* Data Start Date - Default is 2020-01-01
* Data End Date - Default is current date on system
* Filename - Defaults are {ticker}{length}{timeframe}Forecast, Signals, Trends. ex. SPY30DayTrends

Many of these have default values outside of the stock ticker, which is required to run the program. After all values have been provided, the program will pull data using the Alpaca API, prepare it, use it with the Prophet model, and save a forecast plot and a trend plot to the 'imgs' folder. Program now creates a third plot displaying EMA 14 and EMA 28 as well as buy and sell signals for a basic trade strategy recommendation.

Example outputs of the code are as follows:

<img src="./imgs/Example_Forecast.png" alt="Forecast Plot" width="1000" height="300">
<img src="./imgs/Example_Signals.png" alt="Signals Plot" width="1000" height="300">
<img src="./imgs/Example_Trends.png" alt="Trend Plot" width="1000" height="600">

---

## Planned features

* Streamlit conversion is beign tested for better UI/UX and speed of use
* ~~Cryptocurrency data compatibility~~
* ~~Pandas TA trading strategy & indicator chart options~~
* Ability to modify indicators
* ~~Buy & sell algorithm to help identify exit and entry points in data~~
* Signal labels
* More comprehensive error messages and sys.exit statements to ensure consistent results
* Possible transition from Alpaca to Yahoo Finance for ease of use
* Possible transition from CLI app to web app for ease of use

---

## Contributors

Brought to you by Majid Kouki. You can reach me at [majidkpy@gmail.com](mailto:majidkpy@gmail.com).

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
