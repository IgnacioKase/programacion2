#Ejercicio 1:

#for i in range(11,20):
    #print(i)

##########################

#Ejercicio 2:

#for i in range(0,7):
#    for j in range(0,i+1):
#        print(i,j)

##########################

#Ejercicio 3:

def domino(n=6):
    for i in range(0,n+1):
        for j in range(0,i+1):
            print(i,j)

#domino(10)

##########################

#Ejercicio 4:

MAX = 10000000
factset = [False for i in range(0,10000000)]
fac = [1,1]

def factorial(n):
    if n == 1:
        return 1
    if n < MAX:
        if factset[n]:
            return fac[n]
    fac.append(n * factorial(n-1))
    factset[n] = True
    return fac[n] 

def ejercicio4():
    m = input()
    for i in range(0,m):
        n = input()
        print(factorial(n))

#print(factorial(5))

##########################

#Ejercicio 5:

def farToCel(c):
    return (c-32)/1.8

def ejercicio5():
    for i in range(0,120,10):
        print(farToCel(i))

#ejercicio5()


##########################

#Ejercicio 6:

def ejercicio6(pesos, tasa, year):
    print(pesos*(1+tasa)**year)

#ejercicio6(4,5,6)

##########################

#Ejercicio 7:

def tri(n):
    sum = 0
    for i in range(0,n+1):
        sum  += i # sum = sum + i
    print("%s - %s" % (n,sum))

def tri_2(n):
    print("%s - %s " % (n,(n*(n+1)/2)))

def ejercicio7():
    n = int(input())
    for i in range(1,n+1):
        tri_2(i)

ejercicio7()

##########################

#Ejercicio 8:

def ejercicio8():
    n = int(input())
    while n < 0:
         n = int(input())
    return n

#print(ejercicio8())

##########################

#Ejercicio 9:



