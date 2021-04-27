# Un programa que realice ciclos, almacene datos de un usuario y realice consultas

class Usuario:

    def __init__(self, clave, nombre, apellido, correo, telefono):
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def setClave(self, clave):
        self.clave = clave

    def getClave(self):
        return self.clave

    def getAtributes(self):
        return f'nombre: {self.nombre}, apellido {self.apellido}, correo {self.correo}, telefono {self.telefono}'

    def __str__(self):
        return self.nombre +' '+ self.apellido


if __name__ == '__main__':
    baseDatos = {}

    rodrigo = Usuario(17, 'rodrigo', 'perez', 'rodrigo@gmail.com', 55464787)
    juan = Usuario(19, 'juan', 'perez', 'juan@gmail.com', 55479787)

    baseDatos[ rodrigo.getClave() ] = rodrigo  # baseDatos[ 17 ] = rodrigo
    baseDatos[juan.getClave()] = juan


    salir = False  # Bandera para salir
    while(salir == False):
        print('1. Busqueda de usuario\n2. Añadir usuario\n3. Modificar usuario\n4. Eliminar usuario\n5. Salir')
        opcion = int(input('Opcion: '))

        if opcion == 1:   # Busqueda
            clave = int(input('Digite usuario: '))

            if clave in baseDatos:
                print(print(baseDatos[clave].getAtributes()))
            else:
                print('Usuario no encontrado')

        if opcion == 2:   # Añadir
            clave = int(input('Clave: '))
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            correo = input('Correo: ')
            telefono = int(input('Telefono: '))

            if clave in baseDatos:
                print('Ya existe un usuario con esta clave')
            else:
                baseDatos[ clave ] = Usuario(clave, nombre, apellido, correo, telefono)

        if opcion == 3:   # Modificar
            clave = int(input('Digite usuario: '))

            if clave in baseDatos:
                print(baseDatos[clave].getAtributes())

                nombre = input('Nombre: ')
                apellido = input('Apellido: ')
                correo = input('Correo: ')
                telefono = int(input('Telefono: '))

                baseDatos[clave].nombre = nombre
                baseDatos[clave].apellido = apellido
                baseDatos[clave].correo = correo
                baseDatos[clave].telefono = telefono

            else:
                print('Usuario no encontrado')

        if opcion == 4:
            clave = int(input('Digite usuario: '))

            if clave in baseDatos:
                print(print(baseDatos[clave].getAtributes()))
                opcion = int(input('Estas seguro que deseas eliminar?\n1. Si\n2. No\nOpcion: '))
                
                if opcion == 1:
                    del baseDatos[clave]
                    print('Usuario eliminado')
                else:
                    print('No se elimino el usuario')

            else:
                print('Usuario no encontrado')

        if opcion == 5:   # Salir
            salir = True
            
        print(f'\nBase de datos: {baseDatos}\n')
