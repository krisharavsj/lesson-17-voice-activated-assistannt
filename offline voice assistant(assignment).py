import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

speak("Offline assistant ready!")

while True:
    command = input("You: ").lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.date.today()
        speak("Today's date is " + str(date))

    elif "hello" in command:
        speak("Hello! How can I help you?")

    elif "exit" in command:
        speak("Goodbye!")
        break

    else:
        speak("I don't understand that.")