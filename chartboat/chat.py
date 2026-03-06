from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the color of orange,explain in one word",
)

print(response.text)