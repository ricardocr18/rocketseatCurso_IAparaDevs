# 🎯 Desafio de Prompt Engineering - Nível 6

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-green.svg)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Descrição do Desafio

O desafio de **Prompt Engineering** envolve o uso estratégico de técnicas específicas para formular comandos (prompts) que permitam extrair as respostas mais precisas, relevantes e detalhadas de uma ferramenta de IA generativa.

Essa prática não apenas refina a interação com a IA, mas também explora ao máximo o potencial da tecnologia, adaptando-a a diferentes contextos e necessidades.

---

## 🎯 Objetivo

Neste desafio, aplicaremos conceitos e metodologias de **Prompt Engineering** para construir prompts eficazes, utilizando como exemplo prático o **ChatGPT** (OpenAI).

O desafio é composto por **4 questões distintas**, cada uma com características específicas que exigem a aplicação de técnicas de Prompt Engineering para obter a melhor resposta possível da ferramenta.

---

## 📚 Técnicas de Prompt Engineering Aplicadas

| Técnica | Descrição | Quando Usar |
|---------|-----------|-------------|
| **Zero-Shot** | Prompt direto sem exemplos | Tarefas simples e bem definidas |
| **Few-Shot** | Prompt com exemplos | Tarefas que precisam de padrão |
| **Chain of Thought** | Raciocínio passo a passo | Problemas que exigem lógica |
| **CIDI** | Context, Instruction, Details, Input | Análises complexas |

---

## 📂 Estrutura do Projeto

```
Nivel6Desafio/
├── questoes/                        # 📋 Questões do desafio
│   ├── questao1_raytracing.md      # Ray Tracing (Zero-Shot)
│   ├── questao2_decomposicao.md    # Decomposição Numérica (Few-Shot + CoT)
│   ├── questao3_maquiavel.md       # Maquiavel em GoT (CIDI)
│   └── questao4_fastapi/           # FastAPI (Prompt Engineering)
│       ├── main.py                 # Aplicação FastAPI
│       └── README.md               # Documentação específica
│
├── respostas/                       # 📝 Respostas das IAs
│   ├── questao1_resposta.md
│   ├── questao2_resposta.md
│   ├── questao3_resposta.md
│   └── questao4_codigo.py
│
├── .env.example                     # Exemplo de variáveis de ambiente
├── .gitignore                       # Arquivos ignorados pelo Git
├── requirements.txt                 # Dependências Python
├── README.md                        # 📖 Esta documentação
└── main.py                          # 🚀 Script principal (opcional)
```

---

## 📋 Questões do Desafio

### 🎨 **Questão 1: Ray Tracing**

**Enunciado:**  
Como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada?

**Técnica:** `Zero-Shot`

**Justificativa:**  
Ray Tracing é uma tecnologia amplamente documentada. A questão é objetiva e não requer exemplos ou contexto adicional.

**Prompt:**
```
Como o algoritmo de Ray Tracing calcula a cor de um pixel em uma imagem renderizada?
```

📄 **[Ver detalhes completos →](questoes/questao1_raytracing.md)**

---

### 🔢 **Questão 2: Decomposição Numérica**

**Enunciado:**  
Obter uma resposta completa de como fazer a decomposição numérica de **142.981**.

**Técnicas:** `Few-Shot` + `Chain of Thought`

**Justificativa:**  
Combinação de exemplos (Few-Shot) com raciocínio passo a passo (Chain of Thought) para garantir precisão e clareza no processo.

**Prompt:**
```
Faça a decomposição numérica de 142.981 passo a passo como nos exemplos abaixo:

Exemplos:
483 = 400 + 80 + 3
7840 = 7000 + 800 + 40 + 0

Agora faça para 142.981:
```

📄 **[Ver detalhes completos →](questoes/questao2_decomposicao.md)**

---

### ⚔️ **Questão 3: Maquiavel em Game of Thrones**

**Enunciado:**  
Quais personagens de **As Crônicas de Gelo e Fogo** possuem características inspiradas na filosofia de **Maquiavel**?

**Técnica:** `CIDI (Context, Instruction, Details, Input)`

**Justificativa:**  
Análise complexa que requer contexto especializado, instruções claras, detalhamento conceitual e entrada precisa.

**Prompt (estruturado):**

**Context:**
```
Você é um especialista em literatura e filosofia política, com conhecimento profundo 
sobre As Crônicas de Gelo e Fogo de George R.R. Martin e as ideias filosóficas de 
Nicolau Maquiavel.
```

**Instruction:**
```
Identifique e explique quais personagens de As Crônicas de Gelo e Fogo possuem 
características que podem ser associadas à filosofia de Maquiavel, especialmente 
no que se refere à manipulação de poder, moralidade pragmática e estratégias políticas.
```

**Details:**
```
A filosofia de Maquiavel, em especial as ideias expostas em O Príncipe, foca na 
manutenção do poder, a moralidade situacional e o uso da astúcia, manipulação e 
força para alcançar e consolidar o poder.

Ao analisar os personagens, considere:
- Suas atitudes e decisões políticas
- Táticas de manipulação
- Conceitos de Virtù (habilidade estratégica) e Fortuna (acaso/sorte)
```

**Input:**
```
Quais personagens de As Crônicas de Gelo e Fogo possuem características 
inspiradas na filosofia de Maquiavel?
```

📄 **[Ver detalhes completos →](questoes/questao3_maquiavel.md)**

---

### 🚀 **Questão 4: FastAPI - Validação de Item**

**Enunciado:**  
Criar um endpoint com **FastAPI** que valide e processe a entrada de um objeto `Item`.

**Especificações do `Item`:**
- **nome**: `string` (máximo 25 caracteres)
- **valor**: `float` (positivo)
- **data**: `date` (não pode ser futura)

**Requisitos:**
1. Validar os valores recebidos
2. Retornar o item com campo adicional `uuid` (identificador único)

**Técnica:** Prompt Engineering aplicado à geração de código

**Código completo:** 📄 **[Ver implementação →](questoes/questao4_fastapi/main.py)**

**Executar:**
```bash
cd questoes/questao4_fastapi
uvicorn main:app --reload
```

**Documentação:** http://localhost:8000/docs

---

## 🚀 Como Executar

### **1️⃣ Clonar o Repositório**

```bash
git clone -b Nivel6Desafio https://github.com/ricardocr18/rocketseatCurso_IAparaDevs.git Nivel6Desafio
cd Nivel6Desafio
```

### **2️⃣ Criar Ambiente Virtual**

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

### **3️⃣ Instalar Dependências**

```bash
pip install -r requirements.txt
```

### **4️⃣ Configurar Variáveis de Ambiente (Opcional)**

```bash
cp .env.example .env
```

Edite o `.env`:
```env
OPENAI_API_KEY=sk-proj-seu_token_aqui
```

### **5️⃣ Executar FastAPI (Questão 4)**

```bash
cd questoes/questao4_fastapi
python main.py
```

Ou:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Acessar documentação:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 📊 Análise Comparativa das Técnicas

| Questão | Técnica | Complexidade | Contexto Necessário | Exemplos | Resultado |
|---------|---------|--------------|---------------------|----------|-----------|
| **1** | Zero-Shot | ⭐ Baixa | ⭐ Mínimo | ❌ Não | ✅ Direto |
| **2** | Few-Shot + CoT | ⭐⭐ Média | ⭐⭐ Médio | ✅ 2 exemplos | ✅ Detalhado |
| **3** | CIDI | ⭐⭐⭐ Alta | ⭐⭐⭐ Alto | ❌ Não | ✅ Profundo |
| **4** | Code Generation | ⭐⭐⭐ Alta | ⭐⭐⭐ Alto | ✅ Especificações | ✅ Funcional |

---

## 🎓 Conceitos Aplicados

### **Prompt Engineering:**
✅ Zero-Shot Learning  
✅ Few-Shot Learning  
✅ Chain of Thought (CoT)  
✅ CIDI Framework  
✅ Context Management  
✅ Instruction Clarity  

### **Desenvolvimento:**
✅ FastAPI Framework  
✅ Pydantic Validation  
✅ REST API Design  
✅ HTTP Status Codes  
✅ UUID Generation  
✅ Exception Handling  

---

## 📚 Recursos e Referências

### **Prompt Engineering:**
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Learn Prompting](https://learnprompting.org/)
- [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/)

### **FastAPI:**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### **Conceitos Técnicos:**
- [Ray Tracing in One Weekend](https://raytracing.github.io/)
- [O Príncipe - Maquiavel (Gutenberg)](https://www.gutenberg.org/ebooks/1232)
- [A Song of Ice and Fire Wiki](https://awoiaf.westeros.org/)

---

## 🧪 Testes

### **Testar Questão 4 (FastAPI):**

```bash
# Instalar HTTPie (opcional)
pip install httpie

# Teste de sucesso
http POST localhost:8000/item nome="Mouse Gamer" valor=150.00 data="2025-01-01"

# Teste de erro (nome longo)
http POST localhost:8000/item nome="Nome extremamente longo que ultrapassa vinte e cinco caracteres" valor=150.00 data="2025-01-01"

# Teste de erro (data futura)
http POST localhost:8000/item nome="Teclado" valor=200.00 data="2026-12-31"

# Teste de erro (valor negativo)
http POST localhost:8000/item nome="Monitor" valor=-500.00 data="2025-01-01"
```

---

## 📂 Arquivos Gerados

### **Questões (Markdown):**
- ✅ `questoes/questao1_raytracing.md` - Análise Zero-Shot
- ✅ `questoes/questao2_decomposicao.md` - Análise Few-Shot + CoT
- ✅ `questoes/questao3_maquiavel.md` - Análise CIDI
- ✅ `questoes/questao4_fastapi/` - Implementação FastAPI

### **Respostas (Geradas por IA):**
- 📝 `respostas/questao1_resposta.md`
- 📝 `respostas/questao2_resposta.md`
- 📝 `respostas/questao3_resposta.md`
- 📝 `respostas/questao4_codigo.py`

---

## 🎯 Resultados Esperados

### **Questão 1 (Ray Tracing):**
✅ Explicação técnica clara do processo de cálculo de cor  
✅ Descrição dos conceitos de rays, intersections, shading  
✅ Resposta objetiva e direta  

### **Questão 2 (Decomposição):**
✅ Decomposição correta: `142.981 = 100.000 + 40.000 + 2.000 + 900 + 80 + 1`  
✅ Explicação passo a passo do processo  
✅ Formatação consistente com os exemplos  

### **Questão 3 (Maquiavel):**
✅ Análise de personagens: Tywin, Littlefinger, Varys, Cersei, Roose Bolton  
✅ Relação clara com conceitos maquiavélicos (Virtù, Fortuna)  
✅ Exemplos de decisões políticas e manipulações  
✅ Fundamentação teórica sólida  

### **Questão 4 (FastAPI):**
✅ Endpoint funcional `/item` (POST)  
✅ Validações automáticas (nome ≤25, valor >0, data ≤hoje)  
✅ Geração de UUID único  
✅ Documentação automática (Swagger/ReDoc)  
✅ Tratamento de erros (422)  

---

## 🐛 Troubleshooting

### **Erro: ModuleNotFoundError**
```bash
# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

### **Erro: Port 8000 already in use**
```bash
# Usar outra porta
uvicorn main:app --reload --port 8001
```

### **Erro: Pydantic validation error**
```bash
# Verificar formato dos dados enviados
# Exemplo correto:
{
  "nome": "Item",
  "valor": 100.0,
  "data": "2025-01-01"
}
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Ricardo Ribeiro**

[![GitHub](https://img.shields.io/badge/GitHub-ricardocr18-black?logo=github)](https://github.com/ricardocr18)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ricardo%20Ribeiro-blue?logo=linkedin)](https://linkedin.com/in/seu-perfil)

---

## ⭐ Agradecimentos

- **Rocketseat** - Pelo excelente curso de IA para Devs
- **OpenAI** - Pela API GPT poderosa e documentação de Prompt Engineering
- **FastAPI Team** - Pelo framework web moderno e eficiente
- **Comunidade Python** - Pelo suporte e bibliotecas incríveis

---

## 🎯 Roadmap

- [ ] Adicionar testes automatizados (pytest)
- [ ] Criar interface web (Streamlit) para testar prompts
- [ ] Adicionar mais exemplos de técnicas avançadas
- [ ] Integrar com outras ferramentas de IA (Claude, Gemini)
- [ ] Criar comparativo de respostas entre diferentes LLMs
- [ ] Adicionar métricas de qualidade das respostas
- [ ] Criar guia visual de técnicas de Prompt Engineering

---

## 📊 Comparativo de Ferramentas de IA

| Ferramenta | Melhor Para | Limitações |
|------------|-------------|------------|
| **ChatGPT** | Análises gerais, código | Context window |
| **Claude** | Documentos longos, análise profunda | Rate limits |
| **Gemini** | Multimodal, imagens | Disponibilidade |
| **GitHub Copilot** | Código, autocomplete | Contexto limitado |

---

<div align="center">

### ⭐ Se este projeto foi útil, deixe uma estrela no repositório! ⭐

**Desenvolvido com 💙 por [Ricardo Ribeiro](https://github.com/ricardocr18)**

---

### 📖 Projeto do Curso: IA para Devs - Rocketseat

</div>