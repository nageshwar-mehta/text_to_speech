import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3

r = sr.Recognizer()

def record():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source)
                MyText = r.recognize_sphinx(audio)  # Use PocketSphinx for offline recognition
                return MyText
        except sr.RequestError as e:
            print("Could not request results: {0}. Retrying...".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred, please try again.")

def output_text(text):
    with open("Output.txt", "a") as f:  # Use context manager for file operations
        f.write(text)
        f.write("\n")

while True:
    text = record()
    output_text(text)
    print("Wrote text:", text)  # Print the recognized text
