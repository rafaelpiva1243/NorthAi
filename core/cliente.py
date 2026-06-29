from google import genai
import os

cliente =  genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
chat = cliente.chats.create(model="gemini-3-flash-preview")
