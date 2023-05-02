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

# Calculate statistics
users_last_24_hours = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(days=1)]['user'].nunique()
teams_last_24_hours = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(days=1)]['team'].nunique()
users_last_7_days = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(days=7)]['user'].nunique()
teams_last_7_days = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(days=7)]['team'].nunique()
users_last_30_days = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(days=30)]['user'].nunique()
teams_last_30_days = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(days=30)]['team'].nunique()
users_current_year = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(years=1)]['user'].nunique()
teams_current_year = df[df['timestamp'] > dt.datetime.now().date() - pd.DateOffset(years=1)]['team'].nunique()

statistics_output = [
    html.P(f"Users in last 24 hours: {users_last_24_hours}", style={'font-family': 'Arial'}),
    html.P(f"Teams in last 24 hours: {teams_last_24_hours}", style={'font-family': 'Arial'}),
    html.P(f"Users in last 7 days: {users_last_7_days}", style={'font-family': 'Arial'}),
    html.P(f"Teams in last 7 days: {teams_last_7_days}", style={'font-family': 'Arial'}),
    html.P(f"Users in last 30 days: {users_last_30_days}", style={'font-family': 'Arial'}),
    html.P(f"Teams in last 30 days: {teams_last_30_days}", style={'font-family': 'Arial'}),
    html.P(f"Users in current year: {users_current_year}", style={'font-family': 'Arial'}),
    html.P(f"Teams in current year: {teams_current_year}", style={'font-family': 'Arial'}),
]



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
