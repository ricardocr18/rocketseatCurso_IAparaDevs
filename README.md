# 🚀 Desafio RAG - Nível 3

## 📋 Descrição do Desafio

Desenvolvimento de três estruturas distintas de **Recuperação e Geração de Respostas (RAG)** com abordagens diferentes para responder questões relacionadas ao livro **"Os Sertões", de Euclides da Cunha**.

### 🎯 Estruturas Implementadas:

1. **Naive RAG** - Abordagem básica de recuperação e geração
2. **Parent RAG** - Recuperação hierárquica de chunks
3. **Rerank RAG** - Recuperação com re-ranqueamento de resultados

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **LangChain** - Framework para construção de aplicações com LLMs
- **OpenAI API** - Modelo de linguagem GPT
- **ChromaDB** - Banco de dados vetorial
- **FastAPI** - Framework web para API REST
- **LangGraph** - Orquestração de fluxos de trabalho

---

## 📁 Estrutura do Projeto

```
projetoNivel3/
├── src/
│   ├── api/           # API REST com FastAPI
│   ├── chains/        # Chains do LangChain
│   ├── database/      # Conexão com ChromaDB
│   ├── models/        # Modelos de dados
│   └── utils/         # Funções utilitárias
├── vector_db/         # Banco de dados vetorial
├── .env.example       # Exemplo de variáveis de ambiente
├── .gitignore
├── main.py            # Ponto de entrada da aplicação
└── requirements.txt   # Dependências do projeto
```

---

## 🚀 Como Executar

### 1️⃣ **Clonar o repositório**

```bash
git clone -b Nivel3Desafio https://github.com/ricardocr18/rocketseatCurso_IAparaDevs.git Nivel3Desafio
cd Nivel3Desafio
```

### 2️⃣ **Criar ambiente virtual**

```bash
python -m venv .venv
```

**Ativar no Windows:**
```bash
.venv\Scripts\activate
```

**Ativar no Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3️⃣ **Instalar dependências**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Configurar variáveis de ambiente**

Copie o arquivo `.env.example` para `.env` e configure:

```bash
cp .env.example .env
```

Edite o `.env` com suas credenciais:
```env
OPENAI_API_KEY=sua_chave_aqui
```

### 5️⃣ **Executar a aplicação**

```bash
python main.py
```

A API estará disponível em: `http://localhost:8000/message`

---

### Endpoints disponíveis:

```http
POST /query
Content-Type: application/json

{
  "question": "Qual é o tema principal de Os Sertões?",
  "session_id": "1"
}
```

---

## 🎓 Sobre o Desafio

Este projeto faz parte do **Curso RocketSeat - IA para Devs**, especificamente o desafio do **Nível 3**, focado em técnicas avançadas de RAG (Retrieval-Augmented Generation).

### 📚 Fonte de Dados

Livro: **"Os Sertões"** - Euclides da Cunha

---
