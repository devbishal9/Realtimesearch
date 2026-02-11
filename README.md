# Realtimesearch.py

# 🤖 Akira – Real-Time AI Assistant (Groq + SerpAPI)

Akira is a JARVIS-style real-time AI assistant built with Python, powered by Groq’s LLaMA-3.3-70B model, and enhanced with live Google search data via SerpAPI.
It delivers accurate, up-to-date answers by merging real-time search results with intelligent summarization.

# ✨ Key Features

🔎 Real-time Google search integration (SerpAPI)

🧠 Zero-hallucination design (search-based answers only)

⚡ Ultra-fast inference using Groq

💬 Persistent chat memory (JSON)

⏱ Live date & time awareness

📡 Streaming responses

🧹 Clean, concise, professional output

🤖 JARVIS-style assistant behavior

# 🛠 Tech Stack

Python 3.10+

Groq API

LLaMA-3.3-70B-Versatile

SerpAPI (Google Search)

dotenv

requests

JSON (chat memory)

# 📂 Project Structure
.<br>
├── Data/<br>
│   └── ChatLog.json<br>
├── .env<br>
├── main.py<br>
└── README.md<br>

# 🔐 Environment Variables

Create a .env file in the root directory:
```
Username=YourName
Assistantname=Akira
GroqAPIKey=YOUR_GROQ_API_KEY
SERP_API_KEY=YOUR_SERPAPI_KEY
```

#📦 Installation
Install dependencies
```
pip install groq python-dotenv requests google-search-results
```
# 🚀 Usage

Run the assistant:
```
python main.py
```

Enter a query:

ENTER YOUR QUERY: Bitcoin price today


Akira will:

Fetch real-time search data

Merge and summarize verified information

Respond clearly and professionally

# 🧠 Assistant Rules

Uses only real-time search data

Never guesses or hallucinates

If data is missing, responds clearly

No filler text, no disclaimers

English-only responses

Fast, confident, JARVIS-style replies

# 🎯 Design Philosophy

Accuracy over creativity

Real-time data first

Professional assistant behavior

Minimal, efficient responses

Inspired by JARVIS from Iron Man.

# 📜 License

This project is intended for educational and personal use.
You are free to modify and extend it.
