from config.prompts import instruction, contextExtrator
from google.genai import types
import json
from core.cliente import chat

message = None

configContex = types.GenerateContentConfig(
    system_instruction=contextExtrator
)

configResp = types.GenerateContentConfig(
        system_instruction=instruction
    )

contextoData = []
context = chat.send_message(message, config=configContex)

try:
    raw_text = context.text.strip()
    contextJson = json.loads(raw_text)
    contextoData.append(contextJson)
except:
    print("Erro ao gerar json")

if contextoData[0]["objetivo"] == "" or contextoData[0]["ferramentas/ambiente/contexto"] == " " or contextoData[0]["momento/situação_atual"] == "":
        prompt = f"""
            O usuário não forneceu informações suficientes.
            Pergunte APENAS sobre os campos que precisam de mais informações, de forma clara:
        """
        configRespContext = types.GenerateContentConfig(
            system_instruction=prompt
        )
else:
    pass    

