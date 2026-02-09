from google import genai
from google.genai import types
import os
from pyfiglet import Figlet
import json

f = Figlet(font="slant")  # pode mudar a fonte
print(f.renderText("NORTH"))

print("Iniciando a IA...")
print("")
print("Para sair digite (exit)")
print("")


cliente =  genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = cliente.chats.create(model="gemini-3-flash-preview")

instruction = """
        Persona: Você é um assistente de IA que ajuda no direcionamento do usuario para a melhor solução de seu questionamento.
        
        Roteiro: Você deve definir o objetivo do usuario, as ferramentas/ambientes/contexto e o momento/situação atual. E as principais informações nescessarias para o melhor direcionamento de resposta ideal para o usuario.
        Você deve somente mostrar a resposta correta ao usuario quando tiver todo o contexto para gerar a resposta ideal para o usuario. Se não tiver tudo que necessita
        deve perguntar ao usuario.
         
        Objetivo: Com base nessas informações, você deve mostrar ao usuario a melhor resposta para seus objetivos, não trazendo informações irrelevantes ou inproprias para os objetios do usuário.

        Regras: Seja totalmente veridico e honesto com o usuario, não deve invertar ou produzir informações falsas. e seja 100% honesto se criar, especular ou prever sobre algo.
        todas as informações devem ter base cientifica, dados reais, fontes veridicas ou documentos academicos. Todas as respostas devem ser com base na comparação de varia fontes diversas, até chegar na melhor opção.
    """

contextExtrator = """
    Extraia informações do texto do usuário.

    Retorne SOMENTE um JSON válido com os campos definidos.
    Não explique nada.
    Não resolva o problema.

    Campos:
    - objetivo
    - ferramentas/ambiente/contexto
    - momento/situação_atual

    Se não encontrar algum campo, use string vazia "".
    """

configContex = types.GenerateContentConfig(
    system_instruction=contextExtrator
)

configResp = types.GenerateContentConfig(
        system_instruction=instruction
    )



while True:
    contextoData = []

    message = input("> ")
    if message == "exit":
        break

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

            res = chat.send_message_stream(message, config=configRespContext )

            for b in res:
                print(b.text)
    else:
        res = chat.send_message_stream(message, config=configResp)

        for i in res:
            print(i.text)