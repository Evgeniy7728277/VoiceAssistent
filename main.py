
import speech_recognition as sr
import pyttsx3
import os
import webbrowser


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
r = sr.Recognizer()

# Define a function for speaking text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function for recognizing speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return None

# Define a function for setting reminders
def set_reminder():
    speak("What would you like to be reminded about?")
    reminder = recognize_speech()
    if reminder:
        speak("When would you like to be reminded?")
        time = recognize_speech()
        if time:
            speak(f"Okay, I will remind you to {reminder} at {time}")
            # TODO: Implement code for setting a reminder

# Define a function for creating a to-do list
def create_todo_list():
    speak("What tasks would you like to add to your to-do list?")
    tasks = []
    while True:
        task = recognize_speech()
        if not task:
            break
        tasks.append(task)
    speak("Okay, here are the tasks you added to your to-do list:")
    for i, task in enumerate(tasks):
        speak(f"{i+1}. {task}")
    # TODO: Implement code for saving the tasks to a file
    dir_path = "C:\\Users\\EvgeniyBelsky\\Desktop\\Assistent"  #!!! Replace with the path to your directory!!!!!
    file_path = os.path.join(dir_path, "todo_list.txt")
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")
# Define a function for searching the web
def search_web():
    speak("What would you like to search for?")
    query = recognize_speech()
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")

# Define a function for handling user commands
def handle_command(command):
    if "reminder" in command:
        set_reminder()
    elif "plan of day" in command:
        create_todo_list()
    elif "search" in command:
        search_web()
    else:
        speak("Sorry, I didn't understand that. Please try again.")

# Start the assistant
speak("Hello! How can I assist you?")
while True:
    command = recognize_speech()
    if command:
        handle_command(command)
    elif "exit" in command:
        speak("Goodbye!")
        break
