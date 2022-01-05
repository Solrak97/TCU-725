from .Estado import *

#Entry Points para /carga_academica/
class Carga_Academica(MethodView):
    def get(self, year):
        if year is None:
            return render_template('carga_academica.html', 
                Estado=Estado_General(), state = "cargas")
            pass
        else:
            return render_template('carga_academica.html', 
                Estado=Estado_Anual(year), state = "cargas")
            pass
    pass


class Estado_General(Estado):
    def __init__(self, year=None):
        super(Estado_General, self).__init__()
        self.general = True
        data = db.query_data("SELECT * FROM prueba.Cargas_Academicas")
        self.fig_proyecto_genero = proyecto_genero(data);
        self.horas_ciclo = fig_horas_ciclo(data)
        self.proyectos_ano = proyectos_ano(data)
        self.tabla_estado_proyecto = tabla_estado(data)
        self.fig_estado_proyecto = estado_proyecto(data)
        self.tabla_tipo = tabla_tipo(data)
        self.tabla_promedio = tabla_promedio(data)
        pass



class Estado_Anual(Estado_General):
    def __init__(self, year):
        super(Estado_Anual, self).__init__()
        self.year = year
        self.general = False
        data = db.query_data(f'''SELECT * FROM prueba.Cargas_Academicas
        WHERE Year = {year}''')
        self.tabla_proyectos = tabla_proyectos(data)
        pass
    pass


    
def proyectos_ano(data):
    values = data
    values = values.groupby(["Year"])["Year"].count()
    fig = px.bar(values, x = values, y = values.index,
        title='Cantidad de proyectos asignados por año',
        color_discrete_sequence=px.colors.sequential.Aggrnyl,
        orientation='h')
    fig.update_layout(layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        



def proyecto_genero(data):
    values = data['Sexo'].value_counts()
    fig = px.pie(values=values, names = values.index,  
        title='Division de proyectos asignados por genero',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_layout(layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)



def fig_horas_ciclo(data):
    values = pd.DataFrame({'Ciclo': ['Ciclo I', 'Ciclo II', 'Ciclo III'] , 'Horas': [
        data['Horas_Ciclo_I'].sum(),
        data['Horas_Ciclo_II'].sum(),
        data['Horas_Ciclo_III'].sum()
    ]})
    fig = px.histogram(values, x='Ciclo', y='Horas',
        title='Cantidad de horas asignadas por ciclo',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_layout(layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)    
    


def estado_proyecto(data, year=None):
    values = data["Estado"].value_counts()
    fig = px.pie(values=values, names = values.index,  
        title='Estado de proyectos',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_layout(layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


def tabla_promedio(data):
    years = np.round(data.groupby(['Year']).size().mean(), 2)
    investigadores = np.round(data.groupby(['Investigador']).size().mean(), 2)
    ciclo_I = np.round(data["Horas_Ciclo_I"].mean())
    ciclo_II = np.round(data["Horas_Ciclo_II"].mean())
    ciclo_III = np.round(data["Horas_Ciclo_III"].mean())
    
    df = pd.DataFrame({"Categoría": ["Promedio de proyectos inscritos por año", "Promedio de investigadores por proyecto", "I CICLO", "II CICLO", "III CICLO"],
     "Promedio":[years, investigadores, ciclo_I, ciclo_II, ciclo_III]})
    return df


def tabla_tipo(data):
    tipo = data["Vicerrect"]
    conteo = tipo.value_counts()
    normal = np.round(tipo.value_counts(normalize=True) * 100, 1)
    
    inv = conteo["Investigación"] if "Investigación" in conteo.index else 0
    accion = conteo["Acción Social"] if "Acción Social" in conteo.index else 0

    inv_p = normal["Investigación"] if "Investigación" in normal.index else 0
    accion_p = normal["Acción Social"] if "Acción Social" in normal.index else 0

    df = pd.DataFrame({"Tipo": ["Investigación", "Acción Social"],
     "Cantidad": [inv, accion],
      "Porcentaje": [inv_p, accion_p]})
    return df



def tabla_estado(data):
    estado = data["Estado"]
    total = len(estado)
    conteo = estado.value_counts()
    normal = np.round(estado.value_counts(normalize=True) * 100, 1)
    
    vigencia = conteo["VIGENCIA"] if "VIGENCIA" in conteo.index else 0
    vigencia_p = normal["VIGENCIA"] if "VIGENCIA" in normal.index else 0

    carga = conteo["CARGA"] if "CARGA" in conteo.index else 0
    carga_p = normal["CARGA"] if "CARGA" in normal.index else 0

    sobrecarga = conteo["SOBRECARGAS"] if "SOBRECARGAS" in conteo.index else 0
    sobrecarga_p = normal["SOBRECARGAS"] if "SOBRECARGAS" in normal.index else 0

    df = pd.DataFrame(
        {"Cantidad de proyectos activos": [total, 100], 
        "Cantidad de proyectos con vigencia":[vigencia, vigencia_p],
        "Cantidad de proyectos con carga aprovada para el 2022": [carga, carga_p],
        "Cantidad de proyectos con sobrecarga": [sobrecarga, sobrecarga_p]})
    return df


# ====================================================================================================
# Seccion anual

#Tabla de proyectos
def tabla_proyectos(data):
    return data[["Investigador", "Codigo", "Proyecto", "Vicerrect"]]