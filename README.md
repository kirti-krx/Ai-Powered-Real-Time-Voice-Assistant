# AI-Powered Real-Time Voice Assistant 🎤🤖

A real-time **voice-enabled AI assistant** built using **Google Gemini (Generative AI)**, **Google Speech-to-Text**, and **gTTS (Text-to-Speech)**.  
It listens to your voice, processes queries using Gemini, and replies back with a natural-sounding voice — all in real time.  

---

## 🚀 Features

- 🎤 **Real-time voice interaction** – talk to the assistant directly.  
- 🧠 **AI-powered responses** using Google Gemini API.  
- 🔊 **Voice output** with natural-sounding speech (gTTS).  
- 📝 **Conversation context memory** – maintains the flow of the conversation.  
- 🛑 **Exit via voice** – just say "exit" or "bye" to stop.  

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini (Generative AI)** – text generation
- **Google SpeechRecognition API** – real-time voice input  
- **gTTS (Google Text-to-Speech)** – voice output  
- **dotenv** – environment variable handling  

---

## ⚙️ Installation

1. **Clone the repository:**
   bash
   git clone https://github.com/<your-username>/voice-assistant.git
   cd voice-assistant.
2. **Create and activate virtual environment (Mac/Linux)**
   python3 -m venv venv
   source venv/bin/activate
3.**Install dependencies**
   pip install -r requirements.txt
4.**Get your Gemini API key**
   Go to Google AI Studio
   Generate an API key and copy it
5.**Create a .env file**
   GEMINI_KEY=your_api_key_here
6.**Run the assistant**
   python voice.py
   

## 🎤 Usage

1. **The assistant will greet you :**
   Agent: Hello Kirti, how can I help you today?
2.**Speak directly – the assistant listens and responds in real time**
3.**Say "exit", "quit", or "bye" to end the session.**


## 📐 Architecture

Flow:

1.**Speech-to-Text (Google STT): Captures and converts your voice to text.**
2.**Gemini AI: Processes the text and generates a response.**
3.**gTTS: Converts AI response back into voice.**
4.**Audio Output: Plays the generated audio instantly.**


## 📂 Project Structure

voice-assistant/
│── voice.py               # Main script
│── requirements.txt       # Dependencies
│── .env                   # API keys (ignored in Git)
│── README.md               # Documentation
│── architecture.png        # System architecture diagram




