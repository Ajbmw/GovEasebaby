from flask import Flask, render_template, request, jsonify
from app.chatbot import get_service_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_service_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
