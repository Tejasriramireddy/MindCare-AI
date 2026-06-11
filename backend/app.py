from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# 🔑 Groq API Key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return "Mental Health Chatbot Backend Running 👍"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        # 🤖 Groq AI Response
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly mental health support chatbot. Be empathetic, kind, and ask follow-up questions."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Something went wrong in backend 😔"})

if __name__ == "__main__":
    app.run(debug=True)