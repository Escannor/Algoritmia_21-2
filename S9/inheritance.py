class Person:
    '''Clase de Persona
    recibe el nombre y apellido como parametro'''
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, clave):
        super().__init__(fname + ' :C', lname)
        self.carrera = 'cibernetica'
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def setClave(aqui, clave):
        aqui.__clave = clave

    def printname(self):
        self.lastname = 'cualquiera'
        super().printname()
        print("Soy estudiante")


x = Student("Mike", "Olsen", 1704)


print('clave alumno:', x.getClave())
x.setClave(1404)
print('clave alumno:', x.getClave())

x.printname() 