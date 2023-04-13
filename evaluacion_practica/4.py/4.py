#Instalar Tesseract OCR y la biblioteca de Google Cloud para Python:
#pip install pytesseract google-cloud-translate

#Importar las bibliotecas necesarias y autenticar la API de Google Translate:
import io
import os

from google.cloud import translate_v2 as translate
import pytesseract
from PIL import Image

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ruta/a/tu/archivo/de/credenciales.json'

translate_client = translate.Client()
#Leer la imagen y extraer el texto en inglés utilizando Tesseract OCR:
image_path = 'ruta/a/tu/imagen.jpg'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

text = pytesseract.image_to_string(Image.open(io.BytesIO(content)))
#Traducir el texto a español utilizando la API de Google Translate:
result = translate_client.translate(text, target_language='es')

translated_text = result['input'] + '\n' + result['translatedText']

#Escribir el texto en inglés y su traducción al español en un archivo de texto plano:
output_path = 'ruta/a/tu/archivo/de/salida.txt'

with open(output_path, 'w') as output_file:
    output_file.write(translated_text)

