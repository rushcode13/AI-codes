import speech_recognition as sr
import pyttsx3 #engine to iniiate text to speech (TTS) conversion
from googletrans import Translate #google translator API

def speak(text, lang="en"):
    engine= pyttsx3.init()
    engine.setProperty('rate',150)#speed of speech
    voices=engine.getProperty('voices')

    if lang== "en":
        engine.setProperty('voice',voices[0].id)#default lang is eng
    else:
        engine.setProperty('voice',voices[0].id)#fallback to another voice
        engine.say(text)
        engine.runAndWait()

def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak into the microphone in english")
        audio= recognizer.listen(source)
    try:
        print("recognising speech")
        text=recognizer.recognize_google(audio,language="en-US")#use english for peech reconition
        print("You said:-"{text})
        return text
    except sr.UnknownValueError:
        print("could not undertsand this audio")
    except sr.RequestError as e:
        print("API error"{e})
    return ""
def translate_text(text, target_language="es"): #default target language is spanish es
    translator=Translator()
    translation=translator.translate(text, dest=target_language)
    print("Translated text:{translation.text}")
    return translation.text

def display_language_options():

print("???? Available translation languages: ")

print("1. Hindi (hi)")

print("2. Tamil (ta)")

print("3. Telugu (te)")

print("4. Bengali (bn)")

print("5. Marathi (mr)")

print("6. Gujarati (gu)")

print("7. Malayalam (ml)")

print("8. Punjabi (pa)")

# User selects language

choice = input("Please select the target language number (1-8): ")

language_dict = {

"1": "hi",

"2": "ta",

"3": "te",

"4": "bn",

"5": "mr",

"6": "gu",

"7": "ml",

"8": "pa"

}


return language_dict.get(choice, "es") # Default to Spanish if invalid input

# Main function to combine all steps

def main():
    # Step 1: Display language options and get user's choice
    target_language = display_language_options()
    # Step 2: Speech-to-Text (recognizing English speech)
    original_text = speech_to_text()
    if original_text:
    # Step 3: Translate to selected target language
    translated_text = translate_text(original_text, target_language=target_language)
    # Step 4: Text-to-Speech (Translate output and speak it)
    speak(translated_text, language="en") # Speak the translation in English
    print("✅ Translation spoken out!")

if __name__=="__main__":
    main()




