#from google import genai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)
messages=[
        {"role": "system", "content": "You are a helpful assistant."}
    ]

client = OpenAI()

while True:
    user_input = input("You: ")
    if user_input.lower()=='quit':
        break
    messages.append({
        "role": "user",
        "content": user_input
    })
    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages
    )
    print("Bot: ",response.output_text,"\n")

