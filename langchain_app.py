from flask import Flask, render_template, request, jsonify
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


model = ChatOpenAI(model="gpt-4.1-mini")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chain = prompt | model

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=['POST'])
def chat():
    question = request.json['message']
    print(question)
    response = chain.invoke({"question": question})
    return jsonify({"response": response.content})

if __name__ == "__main__":
    app.run(debug=True)