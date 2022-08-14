# Import initial libraries and dependencies
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

# Define a function that uses closing prices and pandas ta to form a basic trading strategy and place buy and sell signals on a chart
def technical_signals(data_df):
    # Define 14-day EMA and 28-day EMA
    ema14 = ta.ema(data_df["close"], length=14)
    ema28 = ta.ema(data_df["close"], length=28)

    # Convert EMAs to dataframes
    ema14_df = pd.DataFrame(ema14)
    ema28_df = pd.DataFrame(ema28)

    # Add EMA indicators to data_df dataframe
    data_df = pd.concat([data_df, ema14_df, ema28_df], axis=1)

    # Create signal lists and trigger for buy and sell signal loop
    buy_signals = []
    sell_signals = []
    trigger = 0

    # Create loop to identify EMA crosses and create buy and sell signals at those points
    for x in range(len(data_df["close"])):
        # If EMA_14 is above or at EMA_28, create a buy signal
        if data_df["EMA_14"].iloc[x] >= data_df["EMA_28"].iloc[x] and trigger != 1:
            buy_signals.append(data_df["close"].iloc[x])
            sell_signals.append(float("NaN"))
            trigger = 1
        # If EMA_14 is below or at EMA_28, create a sell signal
        elif data_df["EMA_14"].iloc[x] <= data_df["EMA_28"].iloc[x] and trigger != -1:
            buy_signals.append(float("NaN"))
            sell_signals.append(data_df["close"].iloc[x])
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
    plt.scatter(x, y1, c='green', s=30, marker="v");
    plt.scatter(x, y2, c='red', marker="^");
    data_df["close"].plot();
    data_df["EMA_14"].plot();
    data_df["EMA_28"].plot();
    plt.legend();
    plt.grid(True)


    return signals_plot