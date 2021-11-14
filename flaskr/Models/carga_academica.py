import plotly.express as px
import plotly
from database import Database
import json
import pandas as pd
import numpy as np

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

class Carga_Academica:
    def __init__(self, year=None):
        db = Database()
        self.carga_academica = db.query_data("SELECT * FROM prueba.Cargas_Academicas")
        
        self.year = year;
        self.anos = self.get_years()
        self.fig_proyecto_genero = self.proyecto_genero(year);
        self.horas_ciclo = self.fig_horas_ciclo(year)
        self.proyectos_ano = self.proyectos_ano()
        self.tabla_estado_proyecto = self.tabla_estado()
        self.fig_estado_proyecto = self.estado_proyecto()
        self.tabla_tipo = self.tabla_tipo()
        self.tabla_promedio = self.tabla_promedio()
        pass


    def proyectos_ano(self):
        values = self.carga_academica
        values = values.groupby(["Year"])["Year"].count()
        fig = px.bar(values, x = values, y = values.index,
            title='Cantidad de proyectos asignados por año',
            color_discrete_sequence=px.colors.sequential.Aggrnyl, 
            labels={
                "y": "Cantidad de proyectos",
                "index": "Año"
            }, orientation='h')
        fig.update_layout(layout)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        



    def proyecto_genero(self, year = None):
        values = self.carga_academica['Sexo'].value_counts()
        fig = px.pie(values=values, names = values.index,  
            title='Division de proyectos asignados por genero',
            color_discrete_sequence=px.colors.sequential.Aggrnyl)
        fig.update_layout(layout)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)



    def fig_horas_ciclo(self, year = None):
        values = pd.DataFrame({'Ciclo': ['Ciclo I', 'Ciclo II', 'Ciclo III'] , 'Horas': [
            self.carga_academica['Horas_Ciclo_I'].sum(),
            self.carga_academica['Horas_Ciclo_II'].sum(),
            self.carga_academica['Horas_Ciclo_III'].sum()
        ]})
        fig = px.histogram(values, x='Ciclo', y='Horas',
            title='Cantidad de horas asignadas por ciclo',
            color_discrete_sequence=px.colors.sequential.Aggrnyl)
        fig.update_layout(layout)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)    
        


    def estado_proyecto(self, year=None):
        values = self.carga_academica["Estado"].value_counts()
        fig = px.pie(values=values, names = values.index,  
            title='Estado de proyectos',
            color_discrete_sequence=px.colors.sequential.Aggrnyl)
        fig.update_layout(layout)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)



    def tabla_promedio(self):
        years = np.round(self.carga_academica.groupby(['Year']).size().mean(), 2)
        investigadores = np.round(self.carga_academica.groupby(['Investigador']).size().mean(), 2)
        ciclo_I = np.round(self.carga_academica["Horas_Ciclo_I"].mean())
        ciclo_II = np.round(self.carga_academica["Horas_Ciclo_II"].mean())
        ciclo_III = np.round(self.carga_academica["Horas_Ciclo_III"].mean())
        
        df = pd.DataFrame({"Categoría": ["Promedio de proyectos inscritos por año", "Promedio de investigadores por proyecto", "I CICLO", "II CICLO", "III CICLO"],
         "Promedio":[years, investigadores, ciclo_I, ciclo_II, ciclo_III]})
        return df


    def tabla_tipo(self):
        tipo = self.carga_academica["Vicerrect"]
        conteo = tipo.value_counts()
        normal = np.round(tipo.value_counts(normalize=True) * 100, 1)

        df = pd.DataFrame({"Tipo": ["Investigación", "Acción Social"],
         "Cantidad": [conteo["Investigación"], conteo["Acción Social"]],
          "Porcentaje": [normal["Investigación"], normal["Acción Social"]]})
        return df



    def tabla_estado(self):
        estado = self.carga_academica["Estado"]
        total = len(estado)
        conteo = estado.value_counts()
        normal = np.round(estado.value_counts(normalize=True) * 100, 1)
        df = pd.DataFrame(
            {"Cantidad de proyectos activos": [total, 100], 
            "Cantidad de proyectos con vigencia":[conteo["VIGENCIA"], normal["VIGENCIA"]],
            "Cantidad de proyectos con carga aprovada para el 2022": [conteo["CARGA"], normal["CARGA"]],
            "Cantidad de proyectos con sobrecarga": [conteo["SOBRECARGAS"], normal["SOBRECARGAS"]]})
        return df



    def get_years(self):
        anos = self.carga_academica.dropna()
        anos = anos["Year"].unique()
        anos.sort()
        
        return anos.astype(int)