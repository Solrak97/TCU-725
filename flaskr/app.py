from flask import Flask, render_template, request
import json
import figuras
import plotly
import os

from Models import carga_academica as CA

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def general():
    fig_estudiantes = figuras.estudiantes_institucion()
    figJSON = json.dumps(fig_estudiantes, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('general.html', state = "general")

@app.route('/estudiantes', methods = ['GET'])
def estudiantes():
    return render_template('estudiantes.html', state = "estudiantes")

@app.route('/tutores', methods = ['GET'])
def tutores():
    return render_template('tutores.html', state = "tutores")

@app.route('/colegios', methods = ['GET'])
def colegios():
    return render_template('colegios.html', state = "colegios")

@app.route('/carga_academica', methods = ['GET'])
def carga_academica():
    year = request.args.get('year')
    carga = CA.Carga_Academica(year)
    return render_template('carga_academica.html', CargaAcademica=carga, state = "cargas")

app.run()