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

# Histogram of user logins over the past year
# Filter data for the past year
past_year = df[df["timestamp"] > pd.Timestamp.now() - pd.DateOffset(years=1)]

# Group data by date and count number of logins
logins_by_date = past_year.groupby(past_year["timestamp"].dt.strftime('%Y-%m'))["user"].count().reset_index()

fig1 = px.histogram(logins_by_date, x="timestamp", y="user", labels={"timestamp": "Month", "user": "logins"},
                   title="Total number of logins by month over the past year", nbins=50)


# Create the Dash app
app = Dash(__name__)


# Define the app layout
app.layout = html.Div(
    children=[
        html.H1(children="User Analytics Dashboard", style={'textAlign': 'center', 'font-family': 'Arial', 'font-size': 40}),
        html.Div(children="Select a time range for the first plot.", style={'font-family': 'Arial'}),
        
        
        # Time range slider
        html.Div([
                dcc.RangeSlider(
                    id='time-range-slider',
                    marks={i: (current_date - pd.DateOffset(days=i)).strftime('%b %d') for i in range(0, 31)},
                    step=1,
                    min=0,
                    max=30,
                    value=[0, 30]
                ),
            ],
            style={'padding':20, 'font': 'Arial', 'font-size': 20}
        ),
        
        # Bar chart for user visits by team
        dcc.Graph(id='user-visits-bar-chart'),

        # Histogram of user logins over the past year
        dcc.Graph(figure=fig1),

        # Statistics
        html.H2(children="Statistics", style={'margin-top':50, 'font-family': 'Arial', 'font-size': 25}),
        html.Div(children = statistics_output, style={'margin-left': 20}),
    ],
)
