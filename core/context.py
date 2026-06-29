from config.prompts import contextExtrator
from google.genai import types
import json
from core.cliente import chat

class Context():
    
    def __init__(self):
        self.configContex = types.GenerateContentConfig(
            system_instruction=contextExtrator
        )


    def message(self, message):
        contextJson = {}

        context = chat.send_message(message, config=self.configContex)

        try:
            raw_text = context.text.strip()
            contextJson = json.loads(raw_text.strip())
        except:
            print("Erro ao gerar json")

        if contextJson["objetivo"] == "" or contextJson["ferramentas/ambiente/contexto"] == " " or contextJson["momento/situação_atual"] == "":
            return contextJson, False
        else:
            return contextJson, True