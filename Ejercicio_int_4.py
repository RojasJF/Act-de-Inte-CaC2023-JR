# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.

from Ejercicio_int_3 import crear_dicc


def contador_dict(dictionario):
  palabra_frecuente= ''
  cantidad=0
  for palabra,valor in dictionario.items():
    if valor > cantidad:
      cantidad= valor
      palabra_frecuente= palabra
  print(f"La palabra mas frecuente es : ( {palabra_frecuente} ) con {cantidad} repeticiones")
  return palabra_frecuente,cantidad

#PRUEBA


# entrada=input('Ingrese su cadena de caracteres: ')
# contador_dict(crear_dicc(entrada))
