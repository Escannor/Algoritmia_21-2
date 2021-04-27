
class Examen:
    def __init__(self, materia, calificacion):
        self.materia = materia
        self.calificacion = calificacion

    def __str__(self):
        return f'{self.materia} {self.calificacion}'

class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre
        self.examenes = []
    
    def agregarExamen(self, nombreExamen, calificacion):
        self.examenes.append(Examen(nombreExamen, calificacion))



listaMaterias = ['Matematicas', 'Ingles', 'Quimica', 'Historia']

luis = Alumno('luis')
i = 0
while (i < len(listaMaterias)):
    calificacion = int(input(f'Ingrese calificacion para {listaMaterias[i]}: '))
    luis.agregarExamen(listaMaterias[i], calificacion)  #Mandar Objeto examen
    i+=1 

print(f'\nExamenes de {luis.nombre}')
for examen in luis.examenes:
    print(examen)