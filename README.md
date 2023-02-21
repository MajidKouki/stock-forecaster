# Stock Forecaster

Web interface application utilizing Prophet library and Yahoo Finance API to provide stock forecasts and trend data. This application was designed for a client with the intention of creating a very simple to use system for non-technical users with minimal setup and detailed instructions while enabling easy access to machine learning tools for time series forecasting and trend analysis.

---

## Technologies

This project leverages python with the following packages:

* [Pandas](https://github.com/pandas-dev/pandas) - For plotting and dataframes.

* [Prophet](https://github.com/facebook/prophet) - For forecasting.

* [Yfinance](https://github.com/ranaroussi/yfinance.git) - For financial data from Yahoo Finance

* [Matplotlib](https://github.com/matplotlib/matplotlib) - For plotting.

* [Numpy](https://github.com/numpy/numpy) - For Prophet usage.

<!-- * [Pandas TA](https://github.com/twopirllc/pandas-ta) - For indicators. -->

* [Streamlit](https://github.com/streamlit/streamlit) - For deploying app in browser.

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
pip install pandas, prophet, matplotlib, datetime, numpy, prophet, python-dotenv, alpaca-trade-api, pandas_ta, streamlit
```

---

## Usage

After the initial setup and install, the program can be run by typing the following into the terminal:

```
streamlit run app.py
```

As the program is opened, a financial disclaimer will appear to ensure the user is aware any risks that may arise from following the advice given by the software. The program intakes the following user data:

* Stock or Crypto data
* Ticker - ex. SPY or BTC
* Timeframe - Either 1Day, 1Hour or 1Min
* Forecast Length - Defaults are 30 days, 720 hours, or 1440 minutes
* Data Start Date - Default is 2020-01-01
* Data End Date - Default is current date on system

Many of these have default values outside of the stock ticker, which is required to run the program. After all values have been provided, the program will pull data using the Alpaca API, prepare it, use it with the Prophet model, and display a forecast plot and a trend plot.

Example outputs of the code are as follows:

<img src="./imgs/web.jpeg" alt="Streamlit Web App" width="700" height="800">
<img src="./imgs/chart.jpeg" alt="Resulting Charts" width="700" height="800">

---

## Contributors

Brought to you by Majid Kouki. You can reach me at [majidkpy@gmail.com](mailto:majidkpy@gmail.com).

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
