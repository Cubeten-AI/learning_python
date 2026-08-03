from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()   
story =""
with open("keibukeuoiba.txt", "r") as file:
    story = file.read()

print(story)
print("ghujoi")
prompt = f'''
You are a helpful assistant of manipur folk story. you were given this story {story}.if you don't know the answer say "I don't know the answer to that question." and if you know the answer then answer the question in a very detailed manner.
'''

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("api_key")   # Replace with your API key
)

print("===== AI Chatbot =====")
print("Type your question below.")
print("Type 'no' when asked if you want to continue.\n")

while True:
    # Ask the user for a question
    user_question = input("You asked question of Keibu_Keioiba: ")
    if "who are you" in user_question.lower():
        print("I am an AI  created by Divason. I can answer your questions and provide information on various topics of queries.")
        continue

    # Skip empty questions
    if user_question.strip() == "":
        print("Please enter a question.")
        continue

    # Send the question to the AI
    completion = client.chat.completions.create(
        model="google/diffusiongemma-26b-a4b-it",
        messages=[
            {"role": "user", "content": user_question},
            {"role": "system", "content": prompt}
        ],
        max_tokens=4096,
        stream=False
    )

    # Display the AI's response
    print("\nAI:", completion.choices[0].message.content)

    # Ask if the user wants to continue
    choice = input("\nDo you have another question? (yes/no): ").strip().lower()

    if choice == "no":
        print("\nThank you for using the AI Chatbot. Goodbye!")
        break
    elif choice == "yes":
        print()
        continue
    else:
        print("\nInvalid choice. The program will exit.")
        break