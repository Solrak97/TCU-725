import plotly.express as px
import plotly
from database import Database
import json
import pandas as pd

layout = {
    #'paper_bgcolor':'rgba(0,0,0,0)',
    #'plot_bgcolor':'rgba(0,0,0,0)',
    'title_x' : 0.5
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
        
        pass


    def proyectos_ano(self):
        values = self.carga_academica
        values = values.groupby(["Year"])["Year"].count()
        fig = px.bar(values, y = values, x = values.index,
            title='Cantidad de horas por ciclo',
            color_discrete_sequence=px.colors.sequential.Aggrnyl, 
            labels={
                "y": "Cantidad de proyectos",
                "index": "Año"
            })
        fig.update_layout(layout)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        



    def proyecto_genero(self, year = None):
        values = self.carga_academica['Sexo'].value_counts()
        fig = px.pie(values=values, names = values.index,  
            title='Proyectos asignados por sexo',
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
            title='Cantidad de horas por ciclo',
            color_discrete_sequence=px.colors.sequential.Aggrnyl)
        fig.update_layout(layout)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)    
        


    def estado_proyecto(self, year=None):
        pass



    def tabla_horas(self):
        pass



    def tabla_tipo(self):
        pass



    def tabla_estado(self):
        pass



    def get_years(self):
        anos = self.carga_academica.dropna()
        anos = anos["Year"].unique()
        anos.sort()
        
        return anos.astype(int)