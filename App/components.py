from dash import html
import dash_bootstrap_components as dbc


def header():
    component = dbc.Jumbotron(className="header", children=
        [
            dbc.Col( html.H1(html.U("TCU-725")))
        ]
    )

    return component


def navBar():
    component = html.Div(id = 'navbar', className="navbar", children = [
        html.H1("Hentai")
    ])

    return component

