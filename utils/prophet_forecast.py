# Import initial libraries and dependencies
from prophet import Prophet
import pandas as pd
from datetime import datetime, timezone
import time

# Create function to prepare data for usage with Prophet and run the model using previously given values.
def prophet_forecast(data_df, length, frequency):
    # Reset dataframe index
    data_df = data_df.reset_index()

    # Rename the columns to fit Prophet model syntax
    data_df.columns = ["ds", "y"]

    # Remove datetimes for Prophet model usage
    data_df["ds"] = data_df["ds"].dt.tz_convert(None)

    # Drop all NaN values, if any
    data_df = data_df.dropna()

    # Call Prophet function and store as an object
    data_model = Prophet()

    # Fit the model
    data_model.fit(data_df)

    # Create future dataframe to hold predictions
    data_future = data_model.make_future_dataframe(periods=length, freq=frequency)

    # Make predictions
    data_forecast = data_model.predict(data_future)

    # Plot Prophet predictions and save as data_plot
    data_plot = data_model.plot(data_forecast, figsize=(15, 10))

    # Reset dataframe index for trend plots
    data_forecast = data_forecast.reset_index()

    # Use plot_components function to plot trends
    trends_plot = data_model.plot_components(data_forecast, figsize=(15, 10))

    # Return data_plot and Trends_plot for saving
    return data_plot, trends_plot