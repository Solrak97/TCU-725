from database import Database

#Entry point de la base de datos
db = Database()

class Estado:
    def __init__(self):
        self.anos = get_years()

#Seleccion de años desde la base de datos
def get_years():
    anos = db.query_data('''
    SELECT DISTINCT Year 
    FROM prueba.Cargas_Academicas 
    WHERE Year IS NOT NULL
    ORDER BY Year;
    ''')
    
    return anos['Year']