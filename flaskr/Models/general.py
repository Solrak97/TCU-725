from .estado import *

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
    tabla = db.query_data('''
        SELECT (SELECT AVG(NotaFinal) FROM prueba.Estudiantes_Colegiales WHERE NotaFinal > 70)AS "Nota promedio de aprobacion",
        (SELECT count(*) FROM prueba.Estudiantes_Colegiales WHERE NotaFinal >= 70 AND Estado = "INACTIVO") AS "Estudiantes aprobados",
        (SELECT count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) FROM prueba.Estudiantes_Colegiales WHERE NotaFinal >= 70 AND Estado = "INACTIVO") AS "Porcentage de aprobados",
        (SELECT count(*) FROM prueba.Estudiantes_Colegiales WHERE NotaFinal < 70 AND Estado = "INACTIVO") AS "Estudiantes reprobados",
        (SELECT count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) FROM prueba.Estudiantes_Colegiales WHERE NotaFinal < 70 AND Estado = "INACTIVO") AS "Porcentage de reprobados",
        (SELECT count(*) FROM prueba.Estudiantes_Colegiales WHERE Estado = "ACTIVO") AS "Estudiantes activos",
        (SELECT count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) FROM prueba.Estudiantes_Colegiales WHERE Estado = "ACTIVO") AS "Porcentage de activos",
        (SELECT count(*) FROM prueba.Estudiantes_Colegiales WHERE Estado = "RETIRO") AS "Estudiantes retiro",
        (SELECT count(*) * 100 / (SELECT count(*) FROM prueba.Estudiantes_Colegiales) FROM prueba.Estudiantes_Colegiales WHERE Estado = "RETIRO" ) AS "Porcentage de retiro"
    ''')
    return tabla.round(2)
    pass


def grafico_estudiantes():
    values = db.query_data('''SELECT Nombre_Institucion as "Institucion", 
        Estudiantes_Decimo + Estudiantes_Undecimo AS "Cantidad de estudiantes" FROM prueba.Colegios_Inscritos;''')
    fig = px.histogram(values, x='Institucion', y='Cantidad de estudiantes',
        title='Cantidad de estudiantes por colegio',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_layout(layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)   
    pass