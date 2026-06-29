from core.cliente import chat
from config.prompts import instruction
from google.genai import types

class Chat():

    def __init__(self):
        self.prompt = f"""
            O usuário não forneceu informações suficientes.
            Pergunte APENAS sobre os campos que precisam de mais informações, de forma clara:
        """

        self.configResp = types.GenerateContentConfig(
                system_instruction=instruction
            )

        self.configRespContext = types.GenerateContentConfig(
            system_instruction=self.prompt
        )

    def context(self, message):
        res = chat.send_message_stream(message, config=self.configResp)
        return res

    def no_context(self, message):
        res = chat.send_message_stream(message, config=self.configRespContext)
        return res