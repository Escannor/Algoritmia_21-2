laptop = 12_000
print('Costo de laptop $', laptop)

sueldoPorSemana = 3_500
print('Sueldo por semana $', sueldoPorSemana)


semanas = 0
for i in range((laptop//sueldoPorSemana)+1):
    semanas += 1
print('Semanas: ', semanas)


semanas = 0
ahorrado = 0
while (ahorrado < laptop):
    semanas += 1
    ahorrado += sueldoPorSemana
print('Semanas: ', semanas)
print('Ahorrado: ',ahorrado)

######################################

print('\n\n')

""" edad = 5
edadAntro = 18
for i in range(100):
    if edad >= edadAntro:
        print('Puedo entrar, edad:',edad)
    else:
        print('No puedo entrar, edad:',edad)
    
    edad += 1 """

edad = 5
edadAntro = 18
while (edad <= edadAntro):  #18
    if edad >= edadAntro:
        print('Puedo entrar, edad:',edad)
    else:
        print('No puedo entrar, edad:',edad)
    
    edad += 1

#####################################

calificacion = 4

while (calificacion < 8):
    print('Hacer examen, calificacion:', calificacion)
    calificacion += 1
print('examen completado') 

################################################################

A = 3
B = 4

while(A<10 or B<10):
    print('A:',A,'B:',B)
    A +=1
    B+=2 
print('A:',A,'B:',B) 

################################################################

print('\n\n')

# continue  //continuar a la siguiente iteracion
# break    //sale del ciclo
# pass     // para rellenar

i = 0
while(i<20):
    i+=1
    if (i%2) == 0:
        pass

    print(' ',i) 

    if (i == 17):
        print('rompe el ciclo')
        break

