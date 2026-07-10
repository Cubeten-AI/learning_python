import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # this loads the.env file

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"# reads from.env
)

completion = client.chat.completions.create(
  model="openai/gpt-oss-120b",
  messages=[
    {"role":"system", "content":"You are Sunibala assistant. You are a B.Tech CSE 7th sem student at MTU from Phayeng, Manipur."},
    {"role":"user", "content":"Who are you?"}
  ],
  temperature=1,
  top_p=1,
  max_tokens=4096,
  stream=False
)

print(completion.choices[0].message.content)