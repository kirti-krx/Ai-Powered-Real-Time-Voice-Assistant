import os
import speech_recognition as sr
from dotenv import load_dotenv
import google.generativeai as genai
from gtts import gTTS

# Load API key
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

# TTS using gTTS and macOS afplay
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    os.system(f"afplay {filename}")  # native Mac audio player

# STT using Google Speech Recognition
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("\n🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Didn't catch that, please repeat...")
        return None
    except sr.RequestError:
        print("⚠️ STT service error!")
        return None

# Context
user_name = "Kirti"
schedule = "Sales Meeting with Taipy at 10:00; Gym with Sophie at 17:00"
conversation_history = [
    f"You are a helpful AI assistant. User is {user_name} and their schedule is: {schedule}"
]

# Greeting
greeting = f"Hello {user_name}, how can I help you today?"
print(f"Agent: {greeting}")
speak(greeting)

# Conversation loop
while True:
    user_input = listen()  # voice input
    if not user_input:
        continue
    if user_input.lower() in ["exit", "quit", "bye"]:
        goodbye = "Goodbye! Have a great day."
        print(f"Agent: {goodbye}")
        speak(goodbye)
        break

    conversation_history.append(f"User: {user_input}")

    # Generate Gemini response
    prompt = "\n".join(conversation_history) + "\nAssistant:"
    try:
        response = model.generate_content(prompt)
        assistant_text = response.text.strip()
    except Exception as e:
        print(f"⚠️ Gemini error: {e}")
        assistant_text = "Sorry, I'm having trouble responding right now."

    conversation_history.append(f"Assistant: {assistant_text}")

    print(f"\nAgent: {assistant_text}")
    speak(assistant_text)
