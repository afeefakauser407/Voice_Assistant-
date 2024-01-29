import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    # Breaking down text into smaller chunks to avoid issues
    chunk_size = 100
    for i in range(0, len(text), chunk_size):
        engine.say(text[i:i+chunk_size])
        engine.runAndWait()

def input_instructions():
    instructions = ""

    try:
        with sr.Microphone() as source:
            print("Listening")
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            speech = listener.listen(source, timeout=5, phrase_time_limit=5)  # Add timeouts
            print("Recognizing...")
            instructions = listener.recognize_google(speech)
            instructions = instructions.lower()
            if "jarvis" in instructions:
                instructions = instructions.replace('jarvis', '')
                print(instructions)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return instructions

def play_jarvis():
    while True:  # Continuous listening
        instructions = input_instructions()
        print(instructions)

        if "play" in instructions:
            song = instructions.replace('play', '')
            talk("Playing " + song)
            pywhatkit.playonyt(song)
        elif 'time' in instructions:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + current_time)
        elif 'date' in instructions:
            current_date = datetime.datetime.now().strftime('%d / %m / %Y')
            talk("Today's date is " + current_date)
        elif 'how are you' in instructions:
            talk('I am fine, thank you. How about you?')
        elif 'what is your name' in instructions:
            talk('I am Jarvis, your assistant. What can I do for you?')
        elif 'who is' in instructions:
            person = instructions.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'stop' in instructions:
            talk('Stopping Jarvis. Goodbye!')
            break
        else:
            talk("Please repeat")

if __name__ == "__main__":
    play_jarvis()
