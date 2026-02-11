from googlesearch import search
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values
import os
import requests

# Load environment variables
env_vars = dotenv_values(".env")
Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")
SERP_API_KEY = env_vars.get("SERP_API_KEY")

client = Groq(api_key=GroqAPIKey)

# System prompt
System = f"""
You are {Assistantname}, an advanced real-time information AI created by {Username}.  
You operate like JARVIS: fast, intelligent, and always based on verified data.

CORE RULES:
1. Always use the real-time search results provided from SerpAPI.  
2. Never hallucinate, guess, or invent information.  
3. If search data is incomplete, respond: "No real-time data available for this query."
4. Present the answer clearly, professionally, and concisely, like JARVIS.
5. Include only meaningful facts: names, numbers, dates, summaries, and key points.
6. Never mention SerpAPI or any internal system process.
7. Do not add unnecessary conversation—respond efficiently like a smart assistant.
8. If the user identity is referenced, treat them as {Username}.

YOUR PRIMARY TASKS:
- Summarize and merge the search results into a single accurate answer.
- Combine search data with system information (time, date, etc.) when relevant.
- Always produce the most relevant and precise information possible.

FORMAT OF ANSWERS:
- Short, direct, confident.
- No filler words.
- No disclaimers.
- No extra politeness.

You are Akira with fully active real-time search capabilities.
Begin answering with maximum accuracy and zero hallucination.
"""


# Ensure folder exists
os.makedirs("Data", exist_ok=True)

# Create ChatLog if missing
if not os.path.exists("Data/ChatLog.json"):
    with open("Data/ChatLog.json", "w") as f:
        dump([], f)


def GoogleSearch(query):
    try:
        url = "https://serpapi.com/search.json"
        params = {
            "q": query,
            "api_key": SERP_API_KEY,
            "num": 5
        }
        res = requests.get(url, params=params).json()

        answer = f"Search results for '{query}':\n[start]\n"

        # Extract organic results
        if "organic_results" in res:
            for item in res["organic_results"]:
                title = item.get("title", "No title")
                snippet = item.get("snippet", "No description")
                link = item.get("link", "")
                answer += f"Title: {title}\nDescription: {snippet}\nLink: {link}\n\n"
            answer += "[end]"
            return answer

        return f"No real-time information found for '{query}'."

    except Exception as e:
        return f"Search error: {e}"




def AnswerModifier(Answer):
    """Remove unnecessary empty lines for professional formatting."""
    lines = Answer.split("\n")
    non_empty = [line.strip() for line in lines if line.strip()]
    return "\n".join(non_empty)


def Information():
    now = datetime.datetime.now()

    info = (
        "Use this real-time information if needed:\n"
        f"Day: {now.strftime('%A')}\n"
        f"Date: {now.strftime('%d')}\n"
        f"Month: {now.strftime('%B')}\n"
        f"Year: {now.strftime('%Y')}\n"
        f"Time: {now.strftime('%H')} hours : {now.strftime('%M')} minutes : {now.strftime('%S')} seconds.\n"
    )
    return info


def RealtimeSearchEngine(prompt):
    # Load chat history
    with open("Data/ChatLog.json", "r") as f:
        messages = load(f)

    # Add user query to history
    messages.append({"role": "user", "content": prompt})

    # Temporary system bot info for this response
    system_messages = [
        {"role": "system", "content": System},
        {"role": "system", "content": GoogleSearch(prompt)},
        {"role": "system", "content": Information()},
    ]

    # Build full input
    full_msg = system_messages + messages

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=full_msg,
        max_tokens=4000,
        temperature=0.7,
        top_p=1,
        stream=True
    )

    Answer = ""

    # Handle streaming text
    for chunk in completion:
        delta = chunk.choices[0].delta.content
        if delta:
            Answer += delta

    # Clean answer
    Answer = Answer.strip().replace("</s>", "")
    final_answer = AnswerModifier(Answer)

    # Save assistant reply
    messages.append({"role": "assistant", "content": final_answer})

    # Save updated chat history
    with open("Data/ChatLog.json", "w") as f:
        dump(messages, f, indent=4)

    return final_answer


if __name__ == "__main__":
    while True:
        prompt = input("\nENTER YOUR QUERY: ")
        reply = RealtimeSearchEngine(prompt)
        print("\n" + reply)
