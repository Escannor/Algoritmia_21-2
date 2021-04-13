
class Examen:
    def __init__(self, materia, calificacion):
        self.materia = materia
        self.calificacion = calificacion

class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.examenes = []
    
    def agregarExamen(self, examen):
        self.examenes.append(examen)



listaMaterias = ['Matematicas', 'Ingles', 'Quimica']

luis = Alumno('luis')
i = 0
while (i < len(listaMaterias)):
    luis.agregarExamen(listaMaterias[i])  #Mandar Objeto examen
    i+=1 