from flask import Flask, render_template, request, Response
import json
import plotly
import os

import Models

estado = Models.Estado()

app = Flask(__name__)

#   Rutas para pagina general
general_view = Models.General.as_view("General")
app.add_url_rule('/', view_func=general_view, methods = ['GET'])


#   Rutas para Estudiantes
estudiantes_view = Models.Estudiantes.as_view("Estudiantes")
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
carga_view = Models.Carga_Academica.as_view("Carga_Academica")
app.add_url_rule('/carga_academica', defaults={'year': None},
                 view_func=carga_view, methods=['GET',])
app.add_url_rule('/carga_academica/<int:year>', view_func=carga_view, methods=['GET',])



#Refactor de la ruta para unificarla en una sola
@app.route("/informe_carga_academica")
def get_informe_carga_general():
    informe_csv = Models.carga_academica.generar_informe(None)
    return Response(informe_csv,
                    mimetype="text/plain",
                    headers={"Content-Disposition":
                            f"attachment;filename=Informe_General.xlsx"})
    pass


@app.route("/informe_carga_academica/<int:year>")
def get_informe_carga_anual(year):
    informe_csv = Models.carga_academica.generar_informe(year)
    return Response(informe_csv,
                    mimetype="text/plain",
                    headers={"Content-Disposition":
                            f"attachment;filename=Informe_{year}.xlsx"})
    pass






if __name__ == '__main__':
    app.run()