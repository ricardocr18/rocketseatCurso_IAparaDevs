# 🚀 Desafio Fine-Tuning - Nível 4

## 📋 Descrição do Desafio

Desenvolvimento de um sistema de **classificação automatizada de mensagens** para um bot de atendimento de uma grande rede varejista que vende produtos domésticos. O projeto utiliza **fine-tuning** de modelos de linguagem da OpenAI para melhorar a precisão na classificação.

### 🎯 Objetivo

Treinar um modelo capaz de classificar mensagens de clientes em **duas categorias**:

- **"venda"**: Mensagens relacionadas à intenção de compra de produtos
- **"suporte"**: Mensagens relacionadas a dúvidas ou problemas com produtos

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **OpenAI API** - Fine-tuning de modelos GPT-3.5-turbo
- **JSONL** - Formato de dados para treinamento
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

---

## 📁 Estrutura do Projeto

```
Nivel4Desafio/
├── src/
│   ├── data/
│   │   ├── treino.jsonl        # 500 exemplos de treinamento
│   │   └── teste.jsonl         # 100 exemplos de validação
│   ├── fine_tune.py            # Script de fine-tuning
│   ├── classify.py             # Script de classificação
│   └── utils.py                # Funções utilitárias
├── .env.example                # Exemplo de variáveis de ambiente
├── .gitignore
├── main.py                     # Ponto de entrada da aplicação
├── test_finetuned.py          # Script de teste do modelo treinado
├── requirements.txt            # Dependências do projeto
└── README.md
```

---

## 📊 Formato dos Dados

Os arquivos JSONL seguem o formato:

```json
{"prompt": "Olá, gostaria de fazer a aquisição do novo produto", "completion": "venda"}
{"prompt": "tudo bom, queria verificar como funciona a TV Smart x0912", "completion": "suporte"}
```

### 📦 Datasets Utilizados:

- **treino.jsonl**: 500 exemplos para treinamento robusto
- **teste.jsonl**: 100 exemplos para validação

*⚠️ Observação: Os dados foram gerados sinteticamente para fins educacionais.*

---

## 🚀 Como Executar

### 1️⃣ **Clonar o repositório**

```bash
git clone -b Nivel4Desafio https://github.com/ricardocr18/rocketseatCurso_IAparaDevs.git Nivel4Desafio
cd Nivel4Desafio
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

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o `.env` e adicione sua chave da OpenAI:

```env
OPENAI_API_KEY=sua_chave_aqui
MODEL_NAME=gpt-3.5-turbo
FINETUNED_MODEL=ft:gpt-3.5-turbo-0125:personal::seu_model_id
```

### 5️⃣ **Executar**

```bash
python main.py
```

### 📚 Conceitos Aplicados:

- ✅ Fine-tuning de Large Language Models (LLMs)
- ✅ Classificação de texto com IA
- ✅ Preparação de datasets para treinamento
- ✅ Avaliação de modelos de ML
- ✅ Integração com APIs de IA

---

## 👨‍💻 Autor

**Ricardo Ribeiro**

---

**⭐ Se este projeto foi útil, deixe uma estrela no repositório!**