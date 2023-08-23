#3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#   cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def crear_dicc(cadena):
  
  palabras= cadena.split()
  cantidad={}
  print ("Diccionario :")
  for i in palabras:
    if i in cantidad:
      cantidad[i] +=1
    else:
      cantidad[i]= 1
  print(f"{cantidad}")
  return cantidad

#PRUEBA

# entrada=input('Ingrese su cadena de caracteres: ')
# crear_dicc(entrada)