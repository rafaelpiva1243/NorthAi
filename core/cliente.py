from google import genai
import os

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    cliente =  genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chat = cliente.chats.create(model="gemini-3-flash-preview")
else:
    raise ValueError("GEMINI_API_KEY não encontrada. Defina a variável de ambiente.")
