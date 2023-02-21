"""Escribir un programa que solicite tres números (enteros positivos) y este pueda determinar el mcm 
    y el mcd (trabajar con factores primos"""

import random
from os import system

def OrdenarArray(vectorInicial):
    vectorOrdenado = []
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
    return vectorOrdenado
    

def RecorrerNumeros(num):
    vectorValores = []

    for item in range(2, num+1):
        
        if VerificarPrimo(item):
            vectorValores.append(item)
    
    return vectorValores

def VerificarPrimo(num):
    if num < 2:
       return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
       return True
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
       return True
    else:       
       return False

def DescomponerNum(num, vector):
    vectorFactores = []

    for item in range(len(vector)):
        while num % vector[item] == 0:
            num = num / vector[item]
            vectorFactores.append(vector[item])
    
    return vectorFactores

def DescomponerDiv(num):
    vectorFactores = []
    pos = num

    for item in range(num):
        if num %  pos == 0:
            vectorFactores.append(pos)
        pos -= 1
    
    return vectorFactores

def GenerarMultiplos(num, cant):
    vectorMultiplos = []
    for item in range(1, cant*10):
        vectorMultiplos.append(num * item)    
    return vectorMultiplos

def CompararListas(lista1, lista2, lista3):
    for item in range(len(lista1)):
        item1 = lista1[item]
        array2 = list(filter(lambda x : x == item1, lista2))
        array3 = list(filter(lambda x : x == item1, lista3))
        if len(array2) > 0 and len(array3) > 0:
            item2 = array2[0]
            item3 = array3[0]
            if item1 == item2 and item2 == item3:
                print(f'Multiplos encontrados: {item1} - {item2} - {item3}')
                return item3

system("cls")

num1 = int(input('ingrese primer numero: '))
num2 = int(input('ingrese segundo numero: '))
num3 = int(input('ingrese tercer numero: '))
print('')

vectoresIngresados = [num1, num2, num3]
vectoresIngresados = OrdenarArray(vectoresIngresados)
num1 = vectoresIngresados[2]
num2 = vectoresIngresados[1]
num3 = vectoresIngresados[0]

vector1 = RecorrerNumeros(num1)
factor1 = DescomponerNum(num1, vector1)
print(f'Primos vector 1 del numero {num1}: {vector1}')
print(f'Factores vector 1: {factor1}')
print('')

vector2 = RecorrerNumeros(num2)
factor2 = DescomponerNum(num2, vector2)
print(f'Primos vector 1 del numero {num2}: {vector2}')
print(f'Factores vector 1: {factor2}')
print('')

vector3 = RecorrerNumeros(num3)
factor3 = DescomponerNum(num3, vector3)
print(f'Primos vector 1 del numero {num3}: {vector3}')
print(f'Factores vector 1: {factor3}')
print('')

lista1 = GenerarMultiplos(num1, num1)
#print(f'Multiplo numero 1: {lista1}')

lista2 = GenerarMultiplos(num2, num1)
#print(f'Multiplo numero 2: {lista2}')

lista3 = GenerarMultiplos(num3, num1)
#print(f'Multiplo numero 3: {lista3}')

mcm = CompararListas(lista1, lista2, lista3)
print(f'el MCM es: {mcm}')
print('')


listaDiv1 = DescomponerDiv(num1)
print(f'Divisores numero 1: {listaDiv1}')

listaDiv2 = DescomponerDiv(num2)
print(f'Divisores numero 2: {listaDiv2}')

listaDiv3 = DescomponerDiv(num3)
print(f'Divisores numero 3: {listaDiv3}')

mcd = CompararListas(listaDiv1, listaDiv2, listaDiv3)
print(f'el MCD es: {mcd}')
print('')





