
from openai import OpenAI
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="poolside/laguna-xs-2.1",
  messages=[{"role":"user","content":"whats your name"}],
  temperature=1,
  top_p=0.95,
  max_tokens=8192,
  
  stream=False
)

print(completion.choices[0].message.content)