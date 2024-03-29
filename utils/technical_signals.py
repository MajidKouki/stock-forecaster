# Import initial libraries and dependencies
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt
import streamlit as st

# Define a function that uses closing prices and pandas ta to form a basic trading strategy and place buy and sell signals on a chart
def technical_signals(data_df, indicator_1, indicator_2, indicator_1_len, indicator_2_len):
    # Check which indicator is chosen and setup info as needed
    if indicator_1 == "EMA":
        ind1 = ta.ema(data_df["Close"], length=indicator_1_len)
    elif indicator_1 == "SMA":
        ind1 = ta.sma(data_df["Close"], length=indicator_1_len)

    if indicator_2 == "EMA":
        ind2 = ta.ema(data_df["Close"], length=indicator_2_len)
    elif indicator_2 == "SMA":
        ind2 = ta.sma(data_df["Close"], length=indicator_2_len)

    # Convert EMAs to dataframes
    ind1_df = pd.DataFrame(ind1)
    ind2_df = pd.DataFrame(ind2)

    # Add EMA indicators to data_df dataframe
    data_df = pd.concat([data_df, ind1_df, ind2_df], axis=1)

    data_df.columns = ['Close','ind1','ind2']

    # Create signal lists and trigger for buy and sell signal loop
    buy_signals = []
    sell_signals = []
    trigger = 0

    # Create loop to identify EMA crosses and create buy and sell signals at those points
    for x in range(len(data_df["Close"])):
        # If EMA_14 is above or at EMA_28, create a buy signal
        if data_df["ind1"].iloc[x] >= data_df["ind2"].iloc[x] and trigger != 1:
            buy_signals.append(data_df["Close"].iloc[x])
            sell_signals.append(float("NaN"))
            trigger = 1
        # If EMA_14 is below or at EMA_28, create a sell signal
        elif data_df["ind1"].iloc[x] <= data_df["ind2"].iloc[x] and trigger != -1:
            buy_signals.append(float("NaN"))
            sell_signals.append(data_df["Close"].iloc[x])
            trigger = -1
        else:
            buy_signals.append(float("NaN"))
            sell_signals.append(float("NaN"))

    # Add buy and sell signals to dataframe
    data_df["buy_signals"] = buy_signals
    data_df["sell_signals"] = sell_signals

    # Plot the close, 14-Day EMA and 28-Day EMA as well as a scatter plot of buy and sell signals
    # signals_plot = 

    x=data_df.index
    y1 = data_df["buy_signals"]
    y2 = data_df["sell_signals"]

    signals_plot = plt.figure(figsize=(15, 10));

    # Create legend labels based on indicator intake data
    ind1_leg = str(indicator_1) + " " + str(indicator_1_len)
    ind2_leg = str(indicator_2) + " " + str(indicator_2_len)

    data_df["Close"].plot();
    data_df["ind1"].plot();
    data_df["ind2"].plot();
    plt.scatter(x, y1, c='green', s=60, marker="v");
    plt.scatter(x, y2, c='red', marker="^");
    plt.legend(["Close", ind1_leg, ind2_leg]);
    plt.grid(True)

    return signals_plot