from PIL import Image
from pytesseract import *
from googletrans import Translator

# Establecer ruta de instalación de Tesseract
pytesseract.tesseract_cmd = r'C:\Users\Usuario\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Pasarle la imagen a PIL
img = Image.open("./imagen.jpg")

# pytesseract para extraer el texto de la imagen
resultado = pytesseract.image_to_string(img)

# Instaciar la clase Translator
traductor = Translator()

# traducir el texto extraído de la imagen
resultado_traducido = traductor.translate(resultado, dest='es').text

with open('resultado.txt', mode='w', encoding='utf-8') as file:
    file.write(resultado_traducido)
