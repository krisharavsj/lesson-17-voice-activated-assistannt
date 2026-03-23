import pyttsx3
import random

engine = pyttsx3.init()

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

responses = [
    "That's interesting!",
    "Tell me more!",
    "I like that.",
    "Hmm, okay!",
    "Got it!"
]

speak("Hello! I am your Voice Master AI.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        speak("Goodbye!")
        break

    elif "your name" in user_input.lower():
        speak("I am Voice Master Plus!")

    elif "hello" in user_input.lower():
        speak("Hello there!")

    else:
        speak(random.choice(responses))