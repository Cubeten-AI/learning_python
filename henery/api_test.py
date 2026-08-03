from openai import OpenAI
import os
import sys
from dotenv import load_dotenv

load_dotenv()
_USE_COLOR = sys.stdout.isatty() and os.getenv("NO_COLOR") is None
_REASONING_COLOR = "\033[90m" if _USE_COLOR else ""
_RESET_COLOR = "\033[0m" if _USE_COLOR else ""

client = OpenAI(
  base_url ="https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("api_key")
)
story = ""
with open("story.txt", "r") as f:
   story = f.read()

print("-----------Help desk------------")

while True:
# taking the input from the  user
  user_prompt = input("\nEnter  your question :")

  completion = client.chat.completions.create(
    model="google/diffusiongemma-26b-a4b-it",
    messages=[{"role":"user","content":user_prompt},
            {"role":"system","content":f" Here is a story about keibu keioiba {story}. you are a helpfull assistant for Henery.His full name is Nongmaithem Henery. He lives in Nachou,Bishnupur,Manipur. currently he is pursuing  Btech in RIT,Roorkee. He loves painting making art and sketch. And  give answer in the form of an assitsnt itsself avoiding  giving information about the model. give the answer in an pleasing way. "}],
    temperature=1,
    top_p=1,
    max_tokens=16384,
    seed=42,
  
    stream=False
  )

  # for chunk in completion:
  #   if not getattr(chunk, "choices", None):
  #     continue
  #   if len(chunk.choices) == 0 or getattr(chunk.choices[0], "delta", None) is None:
  #     continue
  #   delta = chunk.choices[0].delta
  #   if getattr(delta, "content", None) is not None:
  #     print(delta.content, end="")

  res = completion.choices[0].message

  print(res)



  choice =input("\n Do you want to ask another question: (yes or no or quit)").strip().lower()


  if choice in ["quit","no"]:
    print("\n Thank you for your  question😊")
    break
  elif choice in ["yes"]:
    continue
  else:
      print("\nInvalid choice.")
      print("\nThank you for your questions. Have a great day! 😊")
      break