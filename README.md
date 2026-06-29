# 🧭 NorthAi

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

```
NorthAi/
│
├── main.py
├── .env
├── requirements.txt
│
├── config/
│   └── prompts.py
│
├── core/
│   ├── cliente.py
│   ├── context.py
│   └── chat.py
│
└── ui/
    └── display.py
```

### `main.py`
Ponto de entrada da aplicação. Inicializa os módulos, exibe o banner e gerencia o loop de interação com o usuário.

### `config/prompts.py`
Contém as strings de instrução da IA — a persona do assistente e o extrator de contexto em JSON.

### `core/cliente.py`
Inicializa o cliente da API Gemini e cria o objeto de chat persistente usado em toda a aplicação.

### `core/context.py`
Envia a mensagem do usuário para extração de contexto, parseia o JSON retornado e verifica se os três campos estão preenchidos.

### `core/chat.py`
Gerencia o envio de mensagens com streaming — uma função para quando o contexto está completo e outra para quando ainda falta informação.

### `ui/display.py`
Responsável pela interface no terminal: banner com `pyfiglet` e impressão das respostas em streaming.

---

## 🚀 Funcionamento

### 1️⃣ Inicialização

Ao executar o programa:

- Um banner estilizado aparece no terminal.
- A API Gemini é configurada usando a variável de ambiente.
- O sistema entra em modo interativo.

### 2️⃣ Fluxo de Conversa

1. O usuário envia uma mensagem.
2. A IA extrai o contexto em JSON (objetivo, ferramentas, situação atual).
3. Se faltar contexto → faz perguntas adicionais.
4. Quando tiver informações suficientes → responde de forma estruturada.

Essa abordagem reduz respostas superficiais e melhora a precisão.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- `google-genai`
- `pyfiglet`
- `python-dotenv`
- Modelo Gemini via API

---

## ⚙️ Instalação e Uso

**1. Clone o repositório**
```bash
git clone https://github.com/rafaelpiva1243/NorthAi
cd NorthAi
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure a chave de API**

Crie um arquivo `.env` na raiz do projeto:
```
GEMINI_API_KEY=sua_chave_aqui
```

**4. Execute**
```bash
python main.py
```

Para sair, digite `exit`.