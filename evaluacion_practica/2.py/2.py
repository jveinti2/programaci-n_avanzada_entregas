#Escriba un programa que realice las siguientes acciones sobre un archivo de texto plano:
#Contar las líneas totales del texto que se encuentra en el archivo.
#Contar las palabras totales del texto, sin contar los espacios.
#Contar los caracteres totales del texto.
#Contar el número de veces que aparece una palabra en el texto del archivo.
#Mostrar esta información en otro archivo de texto plano de salida.

import os

# Función para contar las líneas totales del archivo
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

# Función para contar las palabras totales del archivo
def count_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return len(words)

# Función para contar los caracteres totales del archivo
def count_characters(file_path):
    with open(file_path, 'r') as file:
        characters = file.read().replace(' ', '')
    return len(characters)

# Función para contar el número de veces que aparece una palabra en el archivo
def count_word_occurrences(file_path, word):
    with open(file_path, 'r') as file:
        text = file.read()
        occurrences = text.count(word)
    return occurrences

# Función para contar el número de veces que cada palabra se repite en el archivo
def count_all_word_occurrences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split() # Dividir en lista
        word_counts = {} #Diccionario vacío
        for word in words: # si no está la palabra se inicializa en 1, si está se suma 1
            if word not in word_counts: 
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    return word_counts

# Archivo de entrada
input_file_path = 'archivo_entrada.txt'

# Archivo de salida
output_file_path = 'archivo_salida.txt'

# Realizar conteos y guardar resultados en archivo de salida
with open(output_file_path, 'w') as output_file:
    # Contar líneas
    line_count = count_lines(input_file_path)
    output_file.write('Número total de líneas: ' + str(line_count) + '\n')

    # Contar palabras
    word_count = count_words(input_file_path)
    output_file.write('Número total de palabras: ' + str(word_count) + '\n')

    # Contar caracteres
    character_count = count_characters(input_file_path)
    output_file.write('Número total de caracteres: ' + str(character_count) + '\n')

    # Contar ocurrencias de palabras
    word_occurrences = count_all_word_occurrences(input_file_path)
    output_file.write('Ocurrencias de palabras: ' + str(word_occurrences) + '\n')