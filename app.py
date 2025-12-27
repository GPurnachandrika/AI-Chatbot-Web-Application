from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(message):
    message = message.lower()

    # Greetings
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "Hello! 👋 How can I help you today?"

    # How are you
    if "how are you" in message:
        return "I'm doing great 😊 Thanks for asking!"

    # AI definition
    if "what is ai" in message or "artificial intelligence" in message:
        return (
            "Artificial Intelligence (AI) is a field of computer science "
            "that focuses on creating systems capable of performing tasks "
            "that normally require human intelligence."
        )

    # Name
    if "your name" in message:
        return "I am a simple chatbot built using Python and Flask 🤖"

    # Help
    if "help" in message:
        return "You can ask me about AI, programming, or general questions."

    # Bye
    if any(word in message for word in ["bye", "exit", "quit"]):
        return "Goodbye! 👋 Have a great day."

    # Default fallback
    return "Sorry, I didn't understand that. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please type something."})

    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
