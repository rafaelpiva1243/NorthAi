# NorthAi
📘 NorthAi

Projeto Python simples de assistente de IA baseado no modelo Gemini da Google. Ele funciona em terminal, recebe entradas do usuário e responde usando uma lógica de contexto para direcionar perguntas de forma eficiente.

Objetivo: ajudar o usuário a encontrar a melhor resposta para sua dúvida — mas só quando tiver contexto suficiente (senão, faz perguntas para coletar mais informações).

Estrutura do Projeto

O repositório contém:

NorthAi
├── .gitattributes
├── README.md
├── main.py        ← script principal
└── prompt.txt     ← exemplos e instruções de prompt

O que o código faz

O script main.py:

Exibe um banner estilizado usando pyfiglet com o texto “NORTH”.

Se conecta à API de IA da Google através do pacote google.genai.

Cria um loop interativo no terminal:

O usuário digita um texto.

O script envia esse texto para o modelo de IA pedir contexto (objetivo + ambiente + situação atual).

Se não houver contexto completo, o bot pede mais informações.

Quando tiver tudo, o bot tenta dar uma resposta de acordo com o que foi informado.

Tudo isso é feito usando a API de chats da Google (modelo "gemini-3-flash-preview") e lógica de prompts definida no próprio código.

Como funciona a lógica

O fluxo principal do main.py funciona assim:

1. Inicialização

O programa:

Importa pacotes (google.genai, pyfiglet, etc.).

Mostra “NORTH” com fonte slant.

Inicializa o cliente da Google com a variável de ambiente GEMINI_API_KEY.

Importante: A variável GEMINI_API_KEY precisa estar definida no ambiente antes de rodar.

2. Prompt principal

O prompt define regras:

O assistente deve descobrir objetivo, ferramentas/contexto e situação atual do usuário.

Só responde de forma final quando tiver informações completas.

Caso contrário, faz perguntas de forma clara para coletar dados.

Isso cria um assistente que não “responde instantaneamente”, mas tenta entender o contexto completo primeiro.

prompt.txt — base de instruções

O arquivo prompt.txt mostra exemplos e regras do processo de extração de contexto:

Define como a resposta deve ser guiada.

Mostra uma estrutura ideal de resposta orientada a contexto.

Exemplifica como o assistente deve interagir para obter a informação correta.

Esse arquivo funciona como linha de base para entender a abordagem do bot.

Como usar

Clone o repositório:

git clone https://github.com/rafaelpiva1243/NorthAi


Instale dependências:

pip install google-ai pyfiglet


Defina a chave da Google GenAI no ambiente:

export GEMINI_API_KEY="sua_chave_aqui"


Rode o bot:

python main.py


Comece a digitar perguntas no terminal!
 
