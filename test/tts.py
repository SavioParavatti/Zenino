import pyttsx3
engine = pyttsx3.init()

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

engine.say("Eu vou falar que meu nome é Zé Nino")
engine.runAndWait()