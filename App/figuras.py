import plotly.graph_objects as go
import plotly.express as px
from plotly.graph_objs import Layout
from database import Database

db = Database()

colegios_inscritos = db.query_data('SELECT * FROM Colegios_Inscritos')


layout = {
    #'paper_bgcolor':'rgba(0,0,0,0)',
    #'plot_bgcolor':'rgba(0,0,0,0)',
    'title_x' : 0.5
}

def estudiantes_institucion():
    values = colegios_inscritos[['Nombre_Institucion', 'Estudiantes_Decimo', 'Estudiantes_Undecimo']]
    
    fig = px.histogram(values, x = 'Nombre_Institucion', y = ['Estudiantes_Decimo', 'Estudiantes_Undecimo'],
    title='Cantidad de estudiantes por colego', color_discrete_sequence=px.colors.sequential.Aggrnyl)
    
    fig.update_layout(layout)
    return fig