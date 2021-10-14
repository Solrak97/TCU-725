import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


#from figuras import Figuras
from components import *


#fig = Figuras()

app = dash.Dash(
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)   #initialising dash app
 
app.layout = html.Div(
    [
        header(),
    ]
)

if __name__ == '__main__': 
    app.run_server()