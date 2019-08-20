from math import *

#Ejercicio 1

def imprimir_pares(n,m=0):
    for i in range(m,n+m):
        print(i*2 - m)

#imprimir_pares(25)

#Ejercicio 2

#imprimir_pares(100)

#Ejercicio 3

#imprimir_pares(5, 10)

#Ejercicio 4 and 5 and 6

def sum_rec(n,m=0):
    if n == m + 1:
        return m +1
    return n + sum_rec(n-1,m)

#print(sum_rec(50))

#print(sum_rec(5,3))

#Ejercicio 7 and 8

def nplica(s,n=2):
    if n == 0:
        return ""
    return s + nplica(s,n-1)

#print(nplica("Aloh", 5))

#Ejercicio 9

def suma(a,b=0):
    return a+b

def multiplica(a,b=1):
    return a*b

def divide(a,b=1):
    return a/b

def getOperation(operacion=0,a=0,b=0):
    if operacion == 1:
        print(suma(a,b))
    elif operacion == 2:
        print(suma(a,-b))
    elif operacion == 3:
        print(multiplica(a,b))
    elif operacion == 4:
        print(divide(a,b))
    elif operacion == 5:
        return True
    return False

def getInput():
    salir = False
    while not salir:
        operacion = input("1.Suma\n2.Resta\n3.Multiplica\n4.Divide\n5.Salir\n")
        a=b=0
        if operacion != 5:
            a = input()
            b = input()
        salir = getOperation(operacion,a,b)

getInput()
