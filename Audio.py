import pyttsx3

texto="Hello world"
engine= pyttsx3.init()
engine.say(texto)
engine.runAndWait()