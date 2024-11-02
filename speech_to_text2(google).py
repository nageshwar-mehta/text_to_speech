import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
# pip install pyaudio

r = sr.Recognizer()

def record():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Listening...")
                audio2 = r.listen(source2)
                MyText = r.recognize_google_cloud(audio2)  # Use Google Web Speech API
                return MyText

        except sr.RequestError as e:
            print("Could not request results: {0}. Retrying...".format(e))
            continue  # Retry on request error
        except sr.UnknownValueError:
            print("Unknown error occurred, please try again.")

def output_text(text):
    with open("Output.txt", "a") as f:  # Use context manager for file operations
        f.write(text)
        f.write("\n")
    return

while True:
    text = record()
    output_text(text)
    print("Wrote text:", text)  # Print the recognized text
