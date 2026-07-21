import os
from dotenv import load_dotenv


load_dotenv()

a=os.getenv("name")
print(os.getenv("name"))
print(a)