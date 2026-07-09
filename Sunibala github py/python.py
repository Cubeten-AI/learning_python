from google import genai

client = genai.Client(api_key="AQ.Ab8RN6IK5RcRlLofq8VZetiWEgcrwXPrICF8pE5Rg7zcSz3ttA")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)