# hello today we are going to make jarvis


from pyttsx3 import engine

enigne = pyttsx3.init("sapi5")
voices = engine.setProperty("voices")
print(voices[0].id)
enigne.setProperty("voice", voices[0].id)

def speak(audio):
    pass

speak("hello Kaif")
