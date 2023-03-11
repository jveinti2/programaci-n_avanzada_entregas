# Solicitamos una palabra al usuario
palabra = input("Ingresa una palabra: ")

# Convertimos la palabra a minúsculas y eliminamos los espacios
palabra = palabra.lower().replace(" ", "")

# Comparamos la palabra original con su versión invertida
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
