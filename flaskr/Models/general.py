from flask.views import MethodView
from flask import render_template
from .Estado import Estado

import plotly.express as px
import plotly
from database import Database
import json
import pandas as pd
import numpy as np

db = Database()

class General(MethodView):
    def get(self):
        return render_template('general.html', 
            Estado=Estado_General(), state = "general")
        pass


class Estado_General(Estado):
    def __init__(self):
        super(Estado_General, self).__init__()
        self.tabla_estudiantes = tabla_estudiantes()
        self.tabla_aprobacion = tabla_aprobacion()
        self.grafico_estudiantes = grafico_estudiantes()
        pass


def tabla_estudiantes():
    data = db.query_data('''SELECT Nombre_Institucion AS Institucion, 
    Estudiantes_Decimo + Estudiantes_Undecimo AS "Total Estudiantes", 
    Estudiantes_esperados1 + Estudiantes_esperados2 AS "Estudiantes Esperados" 
    FROM prueba.Colegios_Inscritos;''')
    return data
    pass


def tabla_aprobacion():
    aprobacion = db.query_data('''SELECT AVG(NotaFinal) AS "Nota promedio de aprobacion", 0 FROM prueba.Estudiantes_Colegiales WHERE NotaFinal > 70;''')
    aprobados = db.query_data('''SELECT count(*) AS "Estudiantes aprobados", count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) AS "Porcentage de aprobados" FROM prueba.Estudiantes_Colegiales WHERE NotaFinal >= 70 AND Estado = "INACTIVO";''')
    reprobados = db.query_data('''SELECT count(*) AS "Estudiantes reprobados", count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) AS "Porcentage de reprobados" FROM prueba.Estudiantes_Colegiales WHERE NotaFinal < 70 AND Estado = "INACTIVO";''')
    activos = db.query_data('''SELECT count(*) AS "Estudiantes activos", count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) AS "Porcentage de activos"FROM prueba.Estudiantes_Colegiales WHERE Estado = "ACTIVO";''')
    retiros = db.query_data('''SELECT count(*) AS "Estudiantes retiro", count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) AS "Porcentage de retiro" FROM prueba.Estudiantes_Colegiales WHERE Estado = "RETIRO";''')

    aprobacion = aprobacion.round(2)
    aprobados = aprobados.round(2)
    reprobados = reprobados.round(2)
    activos = activos.round(2)
    retiros = retiros.round(2)
    tabla = [aprobacion, aprobados, reprobados, activos, retiros]    
    return tabla
    pass


#Reorganizar las dependencias en un solo archivo, junto con las referencias de estilo
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


def grafico_estudiantes():
    values = db.query_data('''SELECT Nombre_Institucion as "Institucion", 
        Estudiantes_Decimo + Estudiantes_Undecimo AS "Cantidad de estudiantes" FROM prueba.Colegios_Inscritos;''')
    fig = px.histogram(values, x='Institucion', y='Cantidad de estudiantes',
        title='Cantidad de estudiantes por colegio',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_layout(layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)   
    pass