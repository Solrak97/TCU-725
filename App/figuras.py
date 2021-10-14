import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Layout
from database import Database

db = Database()

colegiales = db.query_data('SELECT*FROM Estudiantes_Colegiales')
colegiales_activos = db.query_data('SELECT * FROM Estudiantes_Activos_Colegiales')
estudiantes_tcu = db.query_data('SELECT * FROM Estudiantes_TCU_UCR')
estudiantes_activos_tcu = db.query_data('SELECT * FROM Estudiantes_Activos_TCU_UCR')
colegios_inscritos = db.query_data('SELECT * FROM Colegios_Inscritos')

print(colegios_inscritos.columns)


layout = {
    #'paper_bgcolor':'rgba(0,0,0,0)',
    #'plot_bgcolor':'rgba(0,0,0,0)',
    'title_x' : 0.5
}

class Figuras():
    def estudiantes_sexo(self):
        values = colegiales['Sexo'].value_counts(normalize=True) * 100
        labels = values.index
        fig = px.pie(values=values, names = labels ,title='Distribucion de estudiantes por sexo',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
        
        fig.update_layout(layout)
        return fig

    def estudiantes_notas(self):
        df = colegiales[['PrimerParcial', 'SegundoParcial', 'TercerParcial']]
        fig = px.box(df, title='Distribucion de notas de estudiantes',
        color_discrete_sequence=px.colors.sequential.Aggrnyl)
        
        fig.update_layout(layout)
        return fig

    def estudiantes_institucion(self):
        values = colegiales['Institucion'].value_counts(normalize=True) * 100
        labels = values.index
        fig = px.pie(values=values, names = labels ,title='Distribucion de estudiantes por institucion',
        color_discrete_sequence=px.colors.sequential.Aggrnyl, hole=0.3)
        
        fig.update_layout(layout)
        return fig

    def institucion_niveles(self):
        values = colegios_inscritos[['Nombre_Institucion', 'Estudiantes_Decimo', 'Estudiantes_Undecimo']]
        fig = px.histogram(values, x = 'Nombre_Institucion', y = ['Estudiantes_Decimo', 'Estudiantes_Undecimo'],
        title='Estudiantes por niveles', color_discrete_sequence=px.colors.sequential.Aggrnyl)

        fig.update_layout(layout)
        return fig

    #Este grafico no tiene mucho sentido,
    #Pero es un ejemplo para scatterplot
    def demo_scatter(self):
        fig = px.scatter(colegiales, x = 'PrimerParcial', y = 'SegundoParcial',
        title='Demo Scatter', color_discrete_sequence=px.colors.sequential.Aggrnyl)

        fig.update_layout(layout)
        return fig