import speech_recognition as sr
from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play
import webbrowser
import datetime
import wikipedia
import smtplib
import cv2
from translate import Translator
##from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import pywhatkit as rep 

# from googletrans import Translator

# pip install pyaudio

def escuchar(nombre):
    reconocedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = reconocedor.listen(source, phrase_time_limit=5)

    try:
        comando = reconocedor.recognize_google(audio, language='es')
        print("Has dicho: " + comando)
        if nombre in comando:
            comando = comando.replace(nombre, "").strip()
            return comando
        else:
            return ""
    except sr.UnknownValueError:
        print("No se pudo entender el comando por voz.")
        return ""
    except sr.RequestError:
        print("No se puede obtener respuesta del servicio de reconocimiento de voz.")
        return ""

def hablar(texto):
    tts = gTTS(text=texto, lang='es')
    tts.save("audio.mp3")
    # print(texto)

def reproducir_video(url):
    webbrowser.open(url)

def obtener_hora_actual():
    ahora = datetime.datetime.now()
    hora_actual = ahora.strftime("%H:%M:%S")
    print("La hora actual es:", hora_actual)

def buscar_wikipedia(consulta):
    try:
        respuesta = wikipedia.summary(consulta, sentences=2)
        print("Wikipedia dice:")
        translator = Translator(to_lang="es", from_lang="en")
        traduccion = translator.translate(respuesta)
        print(traduccion)

    except wikipedia.exceptions.DisambiguationError as e:
        print("La consulta es ambigua. Por favor, sé más específico.")
    except wikipedia.exceptions.PageError as e:
        print("No se encontró ninguna página con esa consulta.")

def abrir_google():
    webbrowser.open("https://www.google.com")

def abrir_video_youtube():
    webbrowser.open("https://www.youtube.com/watch?v=9bZkp7q19f0")

def leer_contraseña_desde_archivo(pwd):
    with open(pwd, 'r') as archivo:
        contraseña = archivo.read().strip()        
    return contraseña

def enviar_email(destinatario, asunto, mensaje):
    remitente = "jbecerrap95@gmail.com"
    password = leer_contraseña_desde_archivo("pwd.txt")
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587

    try:
        server = smtplib.SMTP(servidor_smtp, puerto_smtp)
        server.starttls()
        server.login(remitente, password)

        email = f"Subject: {asunto}\n\n{mensaje}"
        server.sendmail(remitente, destinatario, email)
        print("Correo electrónico enviado correctamente.")
    except smtplib.SMTPAuthenticationError as e:
        print("Error de autenticación. Verifica tus credenciales.", str(e))        
    except smtplib.SMTPException as e:
        print("Error al enviar el correo electrónico:", str(e))
    finally:
        server.quit()

def buscar_y_reproducir_video(busqueda):
    rep.playonyt(busqueda)

def tomar_foto():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("foto.png", frame)
        print("Foto tomada correctamente.")
    cam.release()

nombre = "asistente"

##COMANDOS
while True:
    comando = escuchar(nombre).lower()

    if comando:
        if "reproducir video" in comando:
            url = comando.replace("reproducir video", "").strip()
            reproducir_video(url)
        elif "hora actual" in comando:
            obtener_hora_actual()

        elif "buscar en wikipedia" in comando:
            consulta = comando.replace("buscar en wikipedia", "").strip()
            buscar_wikipedia(consulta)

        elif "abrir google" in comando:
            abrir_google()
        elif "enviar correo" in comando:
            destinatario = input("Ingresa el correo del destinatario: ")
            asunto = input("Ingresa el asunto del correo: ")
            mensaje = input("Ingresa el mensaje del correo: ")
            enviar_email(destinatario, asunto, mensaje)
        elif "buscar en youtube" in comando:
            busqueda = comando.replace("buscar en youtube", "").strip()
            buscar_y_reproducir_video(busqueda)
        elif "tomar foto" in comando:
            tomar_foto()

        elif "salir" in comando:
            print("Hasta luego.")
            hablar("Hasta luego.")
            break
        else:
            hablar("Comando no reconocido. Por favor, intenta nuevamente.")
    else:
        print("Esperando a que me llames por mi nombre...")
