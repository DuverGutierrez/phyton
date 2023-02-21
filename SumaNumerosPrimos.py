#Ingresado un numero ‘n’ entero positivo determinar la suma de los primos hasta ese numero
global sumaPrimos
sumaPrimos = 0

def f_verificarPrimo(num):
    print(num)
    if num < 2:
       print(f"El numero {num} es menor de 2")
       return False
    elif num == 2 or num == 3 or num == 5 or num == 7:
       print(f"El numero {num} SI es primo")
       return True
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
       print(f"El numero {num} SI es primo")
       return True    
    else:       
       print(f"El numero {num} No es primo")
       return False

def f_recibeNumero(num):
    while num > 0:
        if f_verificarPrimo(num):
           global sumaPrimos
           sumaPrimos = sumaPrimos + num
        num -= 1

    print(f"La suma de numeros primos es: {sumaPrimos}")

num = f_recibeNumero(int(input("Ingrese numero: ")))
#mañsdas

