from cliente import chat
from context import configContex, configResp, configRespContext
from config.prompts import instruction
from google.genai import types

message = None


prompt = f"""
                O usuário não forneceu informações suficientes.
                Pergunte APENAS sobre os campos que precisam de mais informações, de forma clara:
            """

configResp = types.GenerateContentConfig(
        system_instruction=instruction
    )

configRespContext = types.GenerateContentConfig(
    system_instruction=prompt
)


res = chat.send_message_stream(message, config=configResp)

res = chat.send_message_stream(message, config=configRespContext )