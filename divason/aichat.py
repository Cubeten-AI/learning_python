from openai import OpenAI
import os

# Create the client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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" # Or replace with your API key
)

# Ask the user for input
user_question = input("Enter your question: ")

# Send the user's question to the model
completion = client.chat.completions.create(
    model="google/diffusiongemma-26b-a4b-it",
    messages=[
        {
            "role": "user",
            "content": user_question
        }
    ],
    temperature=1,
    top_p=0.95,
    max_tokens=4096,
    extra_body={
        "chat_template_kwargs": {
            "thinking": True,
            "reasoning_effort": "high"
        }
    },
    stream=False
)

# Print reasoning if available
reasoning = (
    getattr(completion.choices[0].message, "reasoning", None)
    or getattr(completion.choices[0].message, "reasoning_content", None)
)

if reasoning:
    print("\nReasoning:")
    print(reasoning)

# Print the model's response
print("\nAI Response:")
print(completion.choices[0].message.content)