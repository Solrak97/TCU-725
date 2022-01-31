from flask.views import MethodView
from flask import render_template
import plotly.express as px
import plotly
from database import Database
import json
import pandas as pd
import numpy as np

#Layout base para los diseños de graficos
#Podria ser refactorizado a un nuevo archivo
#de estilos

layout = {
    #'paper_bgcolor':'rgba(0,0,0,0)',
    #'plot_bgcolor':'rgba(0,0,0,0)',
    'title_x' : 0.5,
#    'x': 0.5,
#    'y': 0.90,
#    'xanchor': 'center',
#    'yanchor': 'top',
}

margin = {
    'l': 20,
    'r': 20,
    't': 20,
    'b': 20
}

#Entry point de la base de datos
db = Database()

class Estado:
    def __init__(self):
        self.anos = get_years()
        self.instituciones = get_instituciones()

#Seleccion de años desde la base de datos
def get_years():
    anos = db.query_data('''
    SELECT DISTINCT Year 
    FROM prueba.Cargas_Academicas 
    WHERE Year IS NOT NULL
    ORDER BY Year;
    ''')
    
    return anos['Year']


#Con este metodo podemos obtener el ID y nombre, para representar
#el nombre en el tatg y el id en el select
def get_instituciones():
    instituciones = db.query_data('''
    SELECT DISTINCT ID, Nombre_Institucion FROM prueba.Colegios_Inscritos;
    ''')
    return instituciones