from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JKM9NAqJVfMYb3OR7guxRXbemDV5CnkRiFQ3DDs2M-1Q")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)