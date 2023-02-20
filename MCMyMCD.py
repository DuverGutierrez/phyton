"""Escribir un programa que solicite tres números (enteros positivos) y este pueda determinar el mcm 
    y el mcd (trabajar con factores primos"""

import random
from os import system

def RecorrerNumeros(num):
    vectorValores = []

    for item in range(2, num+1):
        #print(f'Posicion: {item}')
        
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

#num = RecorrerNumeros(int(input("digite numero:  ")))

system("cls")

num1 = int(input('ingrese primer numero: '))
vector1 = RecorrerNumeros(num1)
factor2 = DescomponerNum(num1, vector1)
print(f'Primos vector 1 del numero {num1}: {vector1}')
print(f'Factores 2: {factor2}')

