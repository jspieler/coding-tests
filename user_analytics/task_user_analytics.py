"""See README.md for instructions."""
from dash import Dash, html


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
