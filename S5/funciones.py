
def suma(a, b): # Argumentos
    suma = a + b
    print(f"Esto se ejecuta dentro de la funcion {suma}")
    return suma  #Regresar valores


def resta(a=2, b=1): # Argumentos por default
    resta = a - b
    print(f"Esto se ejecuta dentro de la funcion {resta}")
    print(f"a: {a}, b: {b}")
    return resta

def multiply(a, b=1) -> int:
    """Multiplica dos numeros"""

    mult = a * b
    print(f"Esto se ejecuta dentro de la funcion {mult}")
    print(f"a: {a}, b: {b}")
    return mult

def divide(a, b=1):
    div1 = a / b
    div2 = b / a
    print(f"a: {a}, b: {b}")
    return [div1, div2]



suma1 = suma(1, 2)
print(f"Esto se ejecuta fuera de la funcion {suma1}",end="\n\n")

resta1 = resta()
resta1 = resta(5)
resta1 = resta(8, 2)
resta1 = resta(b=4)
resta1 = resta(b=3, a=2)

print("\n")
mult1 = multiply(4, 2)

print("\n")
div1, div2 = divide(4, 2)
print(div1)
print(div2)