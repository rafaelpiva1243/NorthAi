from google import genai
import os

class Cliente():

    def chat():
        cliente =  genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        return cliente.chats.create(model="gemini-3-flash-preview")



