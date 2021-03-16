import random

def repaso(nombre, num_preguntas):
    aciertos = 0
    for i in range(num_preguntas):
        a = random.randint(1,9)
        b = random.randint(1,9)
        print(f"{a}+{b} = ")
        resultado = int(input())
        if validar(a, b, '+', resultado):
            aciertos += 1


    print(f"{nombre} ha conseguido {aciertos}/{num_preguntas}")



def validar(a,b,operador, c):  # 4, 5, '*', 20    | 1,3, '/', 0 | + | -
    if operador == '+':
        if (a + b) == c:
            return True
        else:
            return False



if __name__ == '__main__':
    repaso("Arturo", 3)