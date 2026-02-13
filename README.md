# 📘 NorthAi

Assistente de IA em Python executado via terminal, utilizando o modelo Gemini da Google.  
O foco do projeto é simples: **coletar contexto suficiente antes de entregar uma resposta final**.

A proposta não é apenas responder perguntas, mas direcionar soluções com base em informações completas.

---

## 🧠 Objetivo

O NorthAi foi desenvolvido para funcionar como um assistente orientado a contexto.

Ele estrutura a conversa com base em três pontos fundamentais:

- 🎯 Objetivo do usuário  
- 🛠️ Ferramentas / ambiente disponível  
- 📍 Situação atual  

Enquanto essas informações não estiverem completas, o sistema continua perguntando.  
Quando o contexto está claro, ele entrega uma resposta organizada e direcionada.

---

## 📂 Estrutura do Projeto

NorthAi/
│
├── main.py
├── prompt.txt
├── README.md
└── .gitattributes


### `main.py`
Script principal da aplicação.  
Responsável por:

- Exibir o banner "NORTH" no terminal
- Inicializar o cliente da API Gemini
- Gerenciar o loop de interação com o usuário
- Aplicar a lógica de coleta de contexto

### `prompt.txt`
Arquivo que contém a base estratégica de comportamento da IA:

- Diretrizes de extração de contexto
- Organização esperada das respostas
- Modelo estrutural de interação

---

## 🚀 Funcionamento

### 1️⃣ Inicialização

Ao executar o programa:

- Um banner estilizado aparece no terminal.
- A API Gemini é configurada usando a variável de ambiente.
- O sistema entra em modo interativo.

---

### 2️⃣ Fluxo de Conversa

O funcionamento segue este padrão:

1. O usuário envia uma mensagem.
2. A IA analisa a entrada.
3. Se faltar contexto → faz perguntas adicionais.
4. Quando tiver informações suficientes → responde de forma estruturada.

Essa abordagem reduz respostas superficiais e melhora a precisão.

---

## 🛠️ Tecnologias Utilizadas

- Python
- `google.genai`
- `pyfiglet`
- Modelo Gemini via API

---

## ⚙️ Pré-requisitos

Antes de executar o projeto:

- Python 3 instalado
- Chave de API Gemini
- Variável de ambiente configurada

Exemplo (Linux/macOS):

```bash
export GEMINI_API_KEY="sua_chave_aqui"

git clone https://github.com/rafaelpiva1243/NorthAi

cd NorthAi

pip install google-ai pyfiglet

python main.py

