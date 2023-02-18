"""sumaPrimos = 0

def RecorrerNumeros(num):
    while num > 0:
        if funcion(num):
            global sumaPrimos
            sumaPrimos += num
        num -= 1
    print(f"La suma de numeros primos es: {sumaPrimos}")


def funcion(num):
    print(num)
    if num < 2:
       print(f"El numero {num} es menor que 2"   )
       return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
       print(f"El numero {num} SI es primo")
       return True
    elif num % 2 != 0 & num % 3 != 0 & num % 5 != 0 & num % 7 != 0:
       print(f"El numero {num} SI es primo")
       return True
    else:       
       print(f"El numero {num} NO es prfffffffimo")
       return False

num = RecorrerNumeros(int(input("digite numero:  ")))"""

"""Escribir un algoritmo que calcule los números primos 
de 0 a 100 utilizando el llamado método de la criba de Eratóstenes. 
Este método consiste en definir e inicializar con todos sus elementos 
a True un vector de 100 elementos binarios e ir “tachando” (pasando a False) en pasadas sucesivas 
todos los múltiplos de los números primos (2, 3, 5, 7...) hasta obtener sólo los números primos. 
nota: se emplearán 2 vectores, uno para los números y el otro para los valores booleanos."""

import random

vectorBooleanos = []
vectorValores = []

for item in range(100):
    vectorBooleanos.append(True)

for item in range(100):
    vectorValores.append(random.randint(2, 100))

def RecorrerNumeros():
    for item in range(len(vectorBooleanos)):
        print(f'Posicion: {item}, Valor: {vectorValores[item]}')
        
        if not(funcion(vectorValores[item])):
            vectorBooleanos[item] = False
    
    print(f'vector boleanos: {vectorBooleanos}')
    print(f'vector valores: {vectorValores}')


def funcion(num):
    if num < 2:
       print(f"El numero {num} es menor que 2"   )
       return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
       print(f"El numero {num} SI es primo")
       return True
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
       print(f"El numero {num} SI es primo")
       return True
    else:       
       print(f"El numero {num} NO es primo")
       return False

#num = RecorrerNumeros(int(input("digite numero:  ")))

print(f'vector boleanos: {vectorBooleanos}')
print(f'vector valores: {vectorValores}')
print(f'largo vector boleanos: {len(vectorBooleanos)}')

RecorrerNumeros()