import math
#2. Escribir una función que calcule el mínimo común múltiplo entre dos números
def mcm (x,y):

    MCD=math.gcd(x,y)  
    micomu=int(x*y/math.gcd(x,y)) 
    print(f"El mínimo común múltiplo entre {x} y {y} es {micomu}\n")
    return micomu    


#PRUEBA

# valorx=int(input('Ingrese el primer número '))
# valory=int(input('Ingrese el segundo numero '))
# mcm(valorx,valory)