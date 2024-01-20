import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

def greet():
    return "Hello! How can I assist you today?"

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"The current time is {current_time}."

def get_date():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    return f"Today's date is {current_date}."

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def voice_assistant(command):
    if "hello" in command.lower():
        return greet()
    elif "time" in command.lower():
        return get_time()
    elif "date" in command.lower():
        return get_date()
    elif "search" in command.lower():
        query = command.split("search", 1)[1].strip()
        return search_web(query)
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Initializing Voice Assistant...")

    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    while True:
        with sr.Microphone() as source:
            print("Listening for a command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Processing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)

            response = voice_assistant(command)
            print("Assistant:", response)

            engine.say(response)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()



