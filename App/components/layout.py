from dash import html
import dash_bootstrap_components as dbc
from figuras import *
from dash import dcc




def header():
    component = html.Div(className="header", children=[
        dbc.Row([
            dbc.Col( html.H1(html.U("TCU-725")), width=1.5),
            dbc.Col( [
                html.H3("Éxito en MATEM:"),
                html.H3("Potenciando nuestros futuros estudiantes") 
                ]),
       ])
    ]) 
    return component




def navBar():
    component = dbc.NavbarSimple(children=[
        dbc.NavItem(dbc.NavLink("Información general", href='#')),
        dbc.NavItem(dbc.NavLink("Información del estudiante", href='#')),
        dbc.NavItem(dbc.NavLink("Información de tutores", href='#')),
        dbc.NavItem(dbc.NavLink("Información de colegios", href='#')),
        dbc.NavItem(dbc.NavLink("Cargas Académicas", href='#')),
    ])

    return component



def general():
    component = dbc.Row([
        dbc.Col( html.Img(src="https://i.pinimg.com/originals/55/68/5a/55685ad4baaaf4e1a8a389deb799fcd5.gif", alt="Mapa de Costa Rica", style={"max-width" : "100%",  "max-height" : "100%"}), width=4),
        dbc.Col( dcc.Graph(figure = estudiantes_institucion()), width=4),
        dbc.Col( html.H1(html.U("Tabla")), width=4),
    ])

    return component