"""See README.md for instructions."""
import pandas as pd
import datetime as dt
from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px

# Read the data from data.csv
df = pd.read_csv('data.csv')

# Convert timestamp column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# calculate the offset between the max date and today
offset = dt.datetime.now().date() - df['timestamp'].max().date()

# Add the offset to the timestamp column
df['timestamp'] = df['timestamp'] + offset

# Calculate the current date as the most recent date in the data
current_date = df['timestamp'].max().date()


if __name__ == "__main__":
    # Run this app and visit http://127.0.0.1:8050/ in your web browser.
    app = Dash(__name__)

    app.layout = html.Div(
        children=[
            html.H1(children="User Analytics Dashboard"),
            html.Div(children="Insert your visualizations and the statistics here."),
        ]
    )
    app.run_server(debug=True)
