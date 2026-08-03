import os
from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)


with open("keibu keioiba.txt", "r", encoding="utf-8") as file:
    document = file.read()

messages = [
    {
        "role": "system",
        "content": f"""
You are "Chater Pater AI". Always say this name when user ask about you, don't say your version or any other details just say your name and say i am here to help you and always answer the question askted to you in respectful manner.


Answer the user's questions using the following document.

Document:
{document}

If the answer is not found in the document, say:
"I couldn't find that information in the document."


"""
    }
]

print("Chatbot started! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("Your Question 🗣️: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye 👋!")
        break

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="google/diffusiongemma-26b-a4b-it",
        messages=messages,
        temperature=1,
        max_tokens=1024
    )

    reply = completion.choices[0].message.content
    print("\nAssistant:", reply, "\n")

    messages.append({"role": "assistant", "content": reply})


    