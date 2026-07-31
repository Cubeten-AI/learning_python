import os
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

messages = []

print("Chatbot started! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("Ask Chatbot : ")

    if user_input.lower() in ["exit", "quit"]:
        print("See you next time!")
        print("If you have more questions in the future, I'll be here to help.")
        break

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="poolside/laguna-xs-2.1",
        messages=messages,
        temperature=1,
        top_p=0.95,
        max_tokens=1024,
        stream=False
    )

    assistant_reply = completion.choices[0].message.content

    print(f"Assistant 🗣️ : {assistant_reply}\n")

    messages.append({"role": "assistant", "content": assistant_reply})