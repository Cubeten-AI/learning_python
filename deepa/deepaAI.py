import os
from openai import OpenAI

# Create client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

try:
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Deepa's assistant. "
                    "If anyone asks about Deepa, answer based on the following information:\n"
                    "- Deepa is from Ngaikhong Khullen, Bishnupur.\n"
                    "- She is studying B.Tech CSE at Manipur Technical University (MTU).\n"
                    "- She is learning AI at Cubeten."
                ),
            },
            {
                "role": "user",
                "content": "Who are you?"
            }
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=4096,
        stream=False,
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print("Error:", e)