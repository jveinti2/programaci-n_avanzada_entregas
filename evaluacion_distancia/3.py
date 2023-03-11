# Creamos una lista de palabras
palabras = ['roma', 'mora', 'perro', 'rata', 'pato', 'topo', 'amor', 'omar']

# Creamos un diccionario para almacenar los anagramas
anagramas = {}

# Iteramos a través de cada palabra en la lista
for palabra in palabras:
    # Convertimos la palabra a una lista de caracteres y la ordenamos alfabéticamente
    lista_palabra = list(palabra)
    lista_palabra.sort()
    palabra_ordenada = ''.join(lista_palabra)

    # Si la palabra ordenada ya está en el diccionario, agregamos la palabra actual a la lista de anagramas
    if palabra_ordenada in anagramas:
        anagramas[palabra_ordenada].append(palabra)
    # Si la palabra ordenada no está en el diccionario, creamos una nueva lista de anagramas para esa palabra ordenada
    else:
        anagramas[palabra_ordenada] = [palabra]

# Imprimimos los anagramas encontrados
for anagrama in anagramas.values():
    if len(anagrama) > 1:
        print(anagrama)
