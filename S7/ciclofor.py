#Imprimir del 1 al 10
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10, end="\n\n")

#range(5) -> [0,1,2,3,4]
#for variable in range(10):
    #
    #
    #

#for (i=0; i<10; i++) {}

#range(start, end, step)

for i in range(1, 11, 1):
    print(i)
print()

#Imprimir los datos de una lista
print()
lista = ['Juan', 'Diego', 'Pedro', 'Jaime']
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print("\nFor posicion")
print(f"longitud de la lista es: {len(lista)}")
for i in range(len(lista)):  #-> [0,1,2,3]
    print(f"posicion {i}, valor {lista[i]}")


print("\nFor item")
print(f"longitud de la lista es: {len(lista)}")
for item in lista:  #['Juan', 'Diego', 'Pedro', 'Jaime']
    print(item)


print()
#Ejecutar una funciona n veces
def funcion_bastante_util(veces):
    print(f"Soy util, lo juro. {veces}")


n_veces = 10

print()
for i in range(n_veces):   #range(n_veces) -> [0,1,2,3,...,n_veces]
    funcion_bastante_util(i)

print("Solo se ejecuta una vez")



print()

diccionario = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'apellido2': 'Prado'
}

print("Items en diccionario:", len(diccionario))

for i in diccionario.keys():
    print(i, ": ", diccionario[i])

print()
for key, value in diccionario.items(): #['nombre', 'Juan']
    print(key, ": ", value)



a, b = [10, 20]



#diccionario.keys() -> [llaves]
#diccionario.values() -> [values]