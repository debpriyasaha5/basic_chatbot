from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv 
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI()

messages = [{
    "role": "system",
    "content": "you are a helpful chat assistant"
}]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=['Post'])
def chat():
    user_input = request.json['message']
    print(user_input)
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages
    )
    return jsonify({"response": response.output_text})

if __name__ == "__main__":
    app.run(debug=True)
