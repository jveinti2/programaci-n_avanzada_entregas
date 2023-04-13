# instalar gtts: pip install gtts
from gtts import gTTS
import os

# Ruta al archivo de texto plano
archivo_texto = 'texto.txt'

# Leer el archivo de texto
with open(archivo_texto, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Crear el objeto de la clase gTTS y generar el archivo de audio
tts = gTTS(texto, lang='es')
tts.save('audio.mp3')

# Reproducir el archivo de audio generado
os.system('start audio.mp3')
