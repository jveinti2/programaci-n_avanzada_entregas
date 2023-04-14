#Escriba un programa que permita generar contraseñas seguras, las contraseñas deben cumplir con las siguientes características:
#Debe incluir letras y números.
#Debe combinar letras mayúsculas y minúsculas.
#La contraseña debe incluir caracteres especiales.
#La longitud de la contraseña debe ser igual o mayor a 8 caracteres.
#No debe tener espacios en blanco.
#La contraseña generada debe mostrarse en consola y guardarse automáticamente en un archivo de texto plano.

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
