from flask.views import MethodView
from flask import render_template
from .Estado import Estado

import plotly.express as px
import plotly
from database import Database
import json
import pandas as pd
import numpy as np

db = Database()

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
    pass

class Estado_Institucion(Estado):
    def __init__(self, ID_institucion):
         super(Estado_Institucion, self).__init__()
    pass