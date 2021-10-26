import dash
from dash import html
import dash_bootstrap_components as dbc

from components.layout import *




app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)   
 
app.layout = html.Div(
    [
        header(),
        navBar(),
        general()
    ]
)

if __name__ == '__main__': 
    app.run_server()