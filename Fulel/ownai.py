import os
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

messages=[]


print("Chatbot started! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("Your Question🗣️ : ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye👋!")
        print("If you have more questions in the future, I'll be here to help.")
        break

    messages.append({"role": "user", "content": user_input})
    messages.append({"role":"system","content":"you are chater pater ai to help a user. Answer every question asked by the user in funny way always. "})

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