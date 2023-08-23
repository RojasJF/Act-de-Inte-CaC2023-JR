import math

#1. Escribir una función que calcule el máximo común divisor entre dos números.
def MCD(x,y):
    RESULTADO=math.gcd(x,y)
    print(f"El máximo común divisor entre {x} y {y} es: {RESULTADO}")
    return RESULTADO   

#Prueba
    
# valorx=int(input('Ingrese el primer numero '))
# valory=int(input('Ingrese el segundo numero '))
# MCD(valorx,valory)
