# 🤖 Jarvis – AI-Powered Personal Voice Assistant (Python)

Jarvis is a **modular, intelligent, voice-enabled personal assistant** built using Python.

It combines **Speech Recognition, Voice Activity Detection (VAD), Large Language Models (LLMs), Memory, and Text-to-Speech (TTS)** into a clean, production-ready pipeline.

This project is designed for **real-time voice interaction**, **high accuracy**, **scalability**, and **developer-grade logging & structure**.

---

## 🚀 Key Features

- 🎙️ **Dynamic Speech-to-Text (STT)** using Whisper  
- 🔇 **Smart Silence Detection** using Silero VAD (no fixed recording limits)  
- 🧠 **LLM-based AI Brain** for human-like responses  
- 💾 **Conversation Memory Module**  
- 🔊 **Natural Text-to-Speech (TTS)**  
- 🧾 **Clean & Structured Logging System**  
- 🧩 **Modular, Scalable Architecture**  
- ⚡ **Low latency, real-time processing**  
- 🛠️ **Developer First Design (Debuggable & Testable)**  

---

## 🏗️ System Architecture

\[ Microphone \]

↓

\[ Silero VAD \] → detects real silence

↓

\[ Whisper STT \] → speech → text

↓

\[ LLM Brain \] → intelligence

↓

\[ Memory Engine \]

↓

\[ Text-to-Speech \]

↓

\[ Speaker Output \]



---

## 🧠 AI Technologies Used

- **Python 3.10.11**
- **Whisper (Speech Recognition)**
- **Silero VAD (Voice Activity Detection)**
- **Large Language Models (LLMs)**
- **NLP & Transformer Models**
- **Wave & Audio Signal Processing**
- **Logging & System Monitoring**

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nmashokkumar/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant
```

---


### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run Jarvis
```bash
python main.py
```

--- 

## Jarvis will:

 - ✅ Listen to your voice
 - ✅ Detect silence automatically
 - ✅ Convert speech to text
 - ✅ Think using LLM
 - ✅ Speak back naturally

---


## 🧾 Logging System

 - Centralized clean logger
 - No unnecessary print statements
 - **Logs saved for:**
   - STT
   - VAD
   - LLM responses
   - Errors & warnings

**This ensures:**

 - ✅ Debuggability
 - ✅ Production readiness
 - ✅ Performance monitoring

### 🛣️ Development Roadmap

 - ✅ Dynamic VAD-based recording
 - ✅ Whisper integration
 - ✅ Modular memory system
 - 🔄 Emotion detection
 - 🔄 Context summarization
 - 🔄 Offline LLM support
 - 🔄 Mobile app integration

## 🧪 Testing Strategy

 - Individual module testing (STT, VAD, TTS)
 - Noise condition testing
 - Latency benchmarking
 - Edge-case silence detection

## 🎯 Target Use Cases

 - Personal AI Assistant
 - Smart Home Automation
 - Voice-based Desktop Control
 - AI Chat Companion
 - Assistive Technology

# 🧑‍💻 Developer

**Ashok Kumar N** - Aspiring Data Scientist & AI Engineer

Project built for learning, research, and real-world AI deployment.
