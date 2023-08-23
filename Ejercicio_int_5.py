# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor n

def get_int():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: El valor ingresado no es válido. Intente nuevamente.")
        return get_int()
    
#PRUEBA


# entero = get_int()
# print(f"Usted ha ingresado el valor entero: {entero}")