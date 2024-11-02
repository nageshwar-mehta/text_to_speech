import wave
import vosk
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3

# Load the model
model = vosk.Model("path_to_model")  # Provide the path to your Vosk model
r = sr.Recognizer()

def record():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source)
                # Save the audio to a WAV file for Vosk
                with wave.open("output.wav", "wb") as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(16000)
                    wf.writeframes(audio.get_raw_data())

            # Transcribe using Vosk
            wf = wave.open("output.wav", "rb")
            rec = vosk.KaldiRecognizer(model, wf.getframerate())
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    return result['text']
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
