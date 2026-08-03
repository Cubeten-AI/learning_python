import os
from openai import OpenAI
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)
with open("kabui keioiba1.txt", "r", encoding="utf-8") as f:
    story = f.read().lower()

print("=" * 55)
print("📖 Welcome to the Kabui Keioiba Story Chatbot!")
print("📚 Ask me anything about the story.")
print("Type 'exit' to quit.")
print("=" * 55)

messages = [
    {
        "role": "system",
        "content": f"""

Be a good story teller and use humour while telling
Answer the user's questions using the following document.

Document:
{story}
If the answer is not found in the document, say:
"sorry, i don't have information about that."


"""
    }
]
while True:
    user_input = input("Ask Anything :")

    if user_input.lower() in ["exit", "quit"]:
        print("have a nice day ,See you next time! 👋!")
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


    