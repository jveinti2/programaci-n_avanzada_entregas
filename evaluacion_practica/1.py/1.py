import random
import string

# Función para generar contraseñas seguras
def generate_password(length=8):
    # Generar una combinación aleatoria de letras, números y caracteres especiales
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation
    all_chars = letters + numbers + special_chars
    password = ''.join(random.sample(all_chars, length))
    return password

# Generar contraseña segura y guardarla en un archivo
password = generate_password()
with open("password.txt", "w") as file:
    file.write(password)

# Imprimir la contraseña generada en la consola
print("Contraseña generada:", password)


#El programa utiliza la biblioteca random para generar contraseñas aleatorias y la biblioteca string para obtener un conjunto de letras, números y caracteres especiales. La función generate_password utiliza la función random.sample para crear una combinación aleatoria de estos caracteres y devuelve la contraseña generada.

#Luego, el programa guarda la contraseña generada en un archivo de texto plano llamado "password.txt" utilizando el método open y write de Python. Finalmente, imprime la contraseña generada en la consola utilizando la función print.