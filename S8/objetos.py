## class <nombre_del_objeto>:
##        def <metodo_del_objeto>(self):

# variable -> atributos
# funciones -> metodos

def hola():
    print("hola a todos")

hola()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def hola(self):
        print("Hola a todos, soy", self.nombre)

    def agregarApellido(self, apellido):
        self.apellido = apellido

    def agregarEdad(self, edad):
        self.edad = edad

    def __str__(self):
        return self.nombre


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


perro = Animal('perro')
perro.edad = 12
perro.raza = 'labrador'




luis = Persona('Luis')
luis.hola()
luis.agregarApellido('Perez')

pedro = Persona('Pedro')
pedro.hola()
pedro.agregarEdad(17)

print(pedro)
pedro.nombre = 'Pablo'
print(pedro)

print(pedro.edad)
pedro.edad = 19
print(pedro.edad)