# print() Imprime en consola lo que tenga dentro
# type() Indica el tipo de dato de la variable

# Integer
entero = 15
print( entero )   # 15
print( type(entero) ,end='\n\n')

#float
flotante = 56.45
flotante = 4565.12345
print( flotante )
print( type(flotante) ,end='\n\n')

# String
cadena = "Hola a todos"
print( cadena )
cadena = 'Estoy aprendiendo Python'
print( cadena )
print( type(cadena) ,end='\n\n')

# Boolean
boleano = True
print( boleano )
boleano = False
print( boleano )
print( type(boleano) ,end='\n\n')


# List
lista = [1, 2, 3, 4, 5]
print( lista )
lista = ['a', 'b', 'c', 'd']
print( lista )
lista = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', True, False]
print( lista )
lista.append('z')
print( lista )
print( type(lista) ,end='\n\n')

# Tuple
tupla = (1, 2, 3, 4, 5)
print( tupla )
tupla = ('a', 'b', 'c', 'd')
print( tupla )
tupla = (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', True, False)
print( tupla )
print( type(tupla) ,end='\n\n')

# Dictionary
diccionario = {
    'nombre': 'Arturo', 
    'apellido': 'Casillas', 
    'edad': 21,
}
print( diccionario )
print( diccionario['nombre'] )
print( diccionario['apellido'] )
diccionario['estatura'] = 1.80
print( diccionario['estatura'] )
diccionario['nombre'] = 'Miguel'
print( type( diccionario) ,end='\n\n')

# sets
setp = {'a', 'b', 'c', 'd', 'e', 'a', 'b'}
print( setp)
setp.add(True)
print( setp )
print( type(setp) ,end='\n\n')