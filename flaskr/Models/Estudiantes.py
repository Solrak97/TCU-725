from .Estado import *

class Estudiantes(MethodView):
     def get(self, ID_institucion):
        if ID_institucion is None:
            return render_template('estudiantes_base.html', 
                Estado=Estado_General(), state = "estudiantes")
            pass
        else:
            return render_template('estudiantes_institucion.html', 
                Estado=Estado_Institucion(ID_institucion), state = "estudiantes")
            pass


class Estado_General(Estado):
    def __init__(self):
         super(Estado_General, self).__init__()
         data = db.query_data('''SELECT * FROM prueba.Estudiantes_Colegiales;''')
    pass



class Estado_Institucion(Estado):
    def __init__(self, ID_institucion):
         super(Estado_Institucion, self).__init__()
         data = db.query_data(f'''SELECT * FROM prueba.Estudiantes_Colegiales WHERE {ID_institucion};''')
    pass