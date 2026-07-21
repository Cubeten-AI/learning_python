from google import genai
from google.genai import types
client = genai.Client(api_key="AQ.Ab8RN6KJGdXTffROkcpH7p41CWJioFPSAl9AZmV4VhQcAR-Ldw")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)