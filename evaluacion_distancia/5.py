# Solicitamos al usuario la cantidad de términos a sumar
n = int(input("Ingresa la cantidad de términos a sumar: "))

# Inicializamos las variables que representan los dos primeros términos de la serie
a, b = 1, 1

# Inicializamos la variable que representa la suma de los términos
suma = 0

# Iteramos para sumar los n términos de la serie
for i in range(n):
    # Si estamos en el primer o segundo término, agregamos 1 a la suma
    if i < 2:
        suma += 1
    else:
        # Calculamos el siguiente término y lo agregamos a la suma
        c = a + b
        suma += c
        # Actualizamos los valores de a y b para el siguiente cálculo
        a, b = b, c

# Imprimimos la suma de los términos
print("La suma de los primeros", n, "términos de la serie es:", suma)
