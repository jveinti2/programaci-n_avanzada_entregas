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

# Archivo de entrada
input_file_path = 'archivo_entrada.txt'

# Archivo de salida
output_file_path = 'archivo_salida_sin_espacios.txt'

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

    # Contar ocurrencias de una palabra
    word = 'palabra'
    word_occurrences = count_word_occurrences(input_file_path, word)
    output_file.write('La palabra "' + word + '" aparece ' + str(word_occurrences) + ' veces')

    #El programa está estructurado en cuatro funciones, cada una de las cuales realiza una operación de conteo sobre el contenido del archivo de entrada. Estas funciones utilizan el comando with open() para abrir el archivo de entrada en modo de lectura y garantizar que se cierre automáticamente una vez que se haya terminado de utilizar.

#La función count_lines() utiliza el método readlines() para leer todas las líneas del archivo y devolver su número mediante la función len(). La función count_words() utiliza el método read() para leer todo el contenido del archivo como una cadena y luego utiliza el método split() para dividir la cadena en palabras, contando el número de palabras mediante la función len(). La función count_characters() utiliza el método read() para leer todo el contenido del archivo como una cadena, y luego elimina los espacios en blanco utilizando el método replace(), contando el número de caracteres mediante la función len(). Finalmente, la función count_word_occurrences() utiliza el método read() para leer todo el contenido del archivo como una cadena y luego utiliza el método count() para contar el número de ocurrencias de una palabra determinada en la cadena.

#En el cuerpo principal del programa, se definen las rutas a los archivos de entrada y salida. Luego se abren el archivo de salida en modo de escritura y se llaman a las funciones de conteo para obtener los resultados. Estos resultados se escriben en el archivo de salida utilizando concatenación de cadenas y el método write().
