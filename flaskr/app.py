from flask import Flask, render_template, request
import json
import figuras
import plotly
import os

from Models import carga_academica as CA
from Models import general as GENERAL
from Models.Estado import Estado

estado = Estado()

app = Flask(__name__)

general_view = GENERAL.General.as_view("General")
app.add_url_rule('/', view_func=general_view, methods = ['GET'])




@app.route('/estudiantes', methods = ['GET'])
def estudiantes():
    return render_template('estudiantes.html', state = "estudiantes", Estado = estado)

@app.route('/tutores', methods = ['GET'])
def tutores():
    return render_template('tutores.html', state = "tutores", Estado = estado)

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