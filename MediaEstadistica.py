"""Escribir un programa que le pregunte al usuario cuantos números quiere generar, 
y este cree un grupo de números de forma aleatoria (enteros positivos), los guarde 
en una lista y muestre por pantalla su media, suma, valor mínimo y máximo, y su mediana."""

import random
import math
from os import system

vectorInicial = []
vectorOrdenado = []
numMin = 0

def GenerarNumeros(num):
    system("cls")
    for item in range(num):
        vectorInicial.append(random.randint(1, 10))
    
    OrdenarArray()

def CalcularMedia(vectorOrdenado):
    sumaItems = 0
    for item in range(len(vectorOrdenado)):
        sumaItems += item
    media = sumaItems / len(vectorOrdenado)
    print(f'Media: {media}')

def CalcularSuma(vectorOrdenado):
    sumaItems = 0
    for item in range(len(vectorOrdenado)):
        sumaItems += item
    print(f'Suma: {sumaItems}')

def CalcularMediana(vectorOrdenado):
    cantidad = len(vectorOrdenado)
    
    if cantidad % 2 == 0:
        mitad = int(cantidad/2)
        suma = (vectorOrdenado[mitad-1] + vectorOrdenado[mitad])/2
        if suma - math.trunc(suma) == 0:
            print(f'Mediana: {math.trunc(suma)}')
        else:
            print(f'Mediana: {suma}')
    else:
        mitad = int((cantidad - 1)/2)
        print(f'Mediana: {vectorOrdenado[mitad]}')
            

def CalcularMinimo(vectorOrdenado):
    numMin = vectorOrdenado[0]

    for item in range(len(vectorOrdenado)):
        if vectorOrdenado[item] < numMin:
                numMin = vectorOrdenado[item]
    print(f'numero menor: {numMin}')

def CalcularMayor(vectorOrdenado):
    numMax = vectorOrdenado[0]
    
    for item in range(len(vectorOrdenado)):
        if vectorOrdenado[item] > numMax:
                numMax = vectorOrdenado[item]
    print(f'numero mayor: {numMax}')


def OrdenarArray():
    print(f'vectorInicial {vectorInicial}')

    global numMin
    numMin = vectorInicial[0]

    for item in range(len(vectorInicial)):

        for item1 in range(len(vectorInicial)):

            if vectorInicial[item1] < numMin:
                numMin = vectorInicial[item1]
        vectorInicial.remove(numMin)
        vectorOrdenado.append(numMin)
        
        if len(vectorInicial) > 0:
            numMin = vectorInicial[0]

    print(f'vectorOrdenado {vectorOrdenado}')
    print('')    
    
    CalcularMedia(vectorOrdenado)
    CalcularSuma(vectorOrdenado)
    CalcularMinimo(vectorOrdenado)
    CalcularMayor(vectorOrdenado)    
    CalcularMediana(vectorOrdenado)



num = GenerarNumeros(int(input("Indique cantidad de numeros a generar: ")))