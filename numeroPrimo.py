#Ingresado un numero ‘n’ entero positivo determinar si este es primo o no.

def funcion(num):
    print(num)
    if num < 2:
       return "El numero debe ser mayor o igual a 2"
    elif num == 2 or num == 3 or num == 5 or num == 7:
       return f"El numero {num} SI es primo"    
    elif num % 2 != 0 & num % 3 != 0 & num % 5 != 0 & num % 7 != 0:
       return f"El numero {num} SI es primo"
    else:       
       return f"El numero {num} NO es prfffffffimo"


num = int(input("digite numero:  "))

print(funcion(num))