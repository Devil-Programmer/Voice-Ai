import speech_recognition as sr
import pyttsx3
import os

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# List available voices (optional)
voices = engine.getProperty('voices')

# Set a specific voice (change '0' to the index of the voice you want to use)
engine.setProperty('voice', voices[0].id)  # You may need to change the index

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to execute commands
def execute_command(command):
    if "open notepad" in command:
        os.system("notepad.exe")
    elif "open calculator" in command:
        os.system("calc.exe")
    # Add more commands here

# Main loop
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        # Recognize speech
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        # Execute command based on recognized speech
        execute_command(command)

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print(e)
        #try a new voice ai
