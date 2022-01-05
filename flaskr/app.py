from flask import Flask, render_template, request
import json
import plotly
import os

from Models import carga_academica as CA
from Models import general as GENERAL
from Models import Estudiantes as ESTUDIANTES
from Models.Estado import Estado

estado = Estado()

app = Flask(__name__)

#   Rutas para pagina general
general_view = GENERAL.General.as_view("General")
app.add_url_rule('/', view_func=general_view, methods = ['GET'])


#   Rutas para Estudiantes
estudiantes_view = ESTUDIANTES.Estudiantes.as_view("Estudiantes")
app.add_url_rule('/estudiantes', defaults={'ID_institucion': None},
                 view_func=estudiantes_view, methods=['GET',])

app.add_url_rule('/estudiantes/<int:ID_institucion>', view_func=estudiantes_view, methods=['GET',])


#   Rutas para tutores
@app.route('/tutores', methods = ['GET'])
def tutores():
    return render_template('tutores.html', state = "tutores", Estado = estado)


#   Rutas para colegios
@app.route('/colegios', methods = ['GET'])
def colegios():
    return render_template('colegios.html', state = "colegios", Estado = estado)




#   Rutas para carga academica
carga_view = CA.Carga_Academica.as_view("Carga_Academica")
app.add_url_rule('/carga_academica', defaults={'year': None},
                 view_func=carga_view, methods=['GET',])
app.add_url_rule('/carga_academica/<int:year>', view_func=carga_view, methods=['GET',])







if __name__ == '__main__':
    app.run()