"""Escribir un programa que le pregunte al usuario cuantos números quiere generar, 
y este cree un grupo de números de forma aleatoria (enteros positivos), los guarde 
en una lista y muestre por pantalla su media, suma, valor mínimo y máximo, y su mediana."""

import random

vectorInicial = []
vectorOrdenado = []
numMin = 0

def GenerarNumeros(num):
    for item in range(num):
        vectorInicial.append(random.randint(1, 100))
    
    OrdenarArray()

def CalcularMedia(vectorOrdenado):
    sumaItems = 0
    for item in range(len(vectorOrdenado)):
        sumaItems += item
    media = sumaItems / len(vectorOrdenado)
    print(f'Media: {media}')

def OrdenarArray():
    print(f'vectorInicial {vectorInicial}')

    global numMin

    numMin = vectorInicial[0]

    for item in range(len(vectorInicial)):

        for item1 in range(len(vectorInicial)):

            if vectorInicial[item1] < numMin:
                numMin = vectorInicial[item1]
        print(f'numero menor: {numMin}')
        vectorInicial.remove(numMin)
        vectorOrdenado.append(numMin)
        
        if len(vectorInicial) > 0:
            numMin = vectorInicial[0]

        print(f'vectorInicial {vectorInicial}')
        print(f'vectorOrdenado {vectorOrdenado}')
        print('')
    
    CalcularMedia(vectorOrdenado)

num = GenerarNumeros(int(input("Indique cantidad de numeros a generar: ")))