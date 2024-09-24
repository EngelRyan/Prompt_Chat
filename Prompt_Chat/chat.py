import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

messages = []

while True:
    user_message = input("You: ")  # Get user input

    messages.append({"role": "user", "content": user_message})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    ai_message = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": ai_message})

    print(f'Chatbot: {ai_message}')

