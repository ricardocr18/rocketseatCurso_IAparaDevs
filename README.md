# 🚀 Desafio Agente de IA - Nível 5
🎮 Sistema Automatizado de Criação de Conteúdo para YouTube Gaming - Nível 5

## 📋 Descrição do Desafio
Sistema multi-agente automatizado que utiliza CrewAI para criar conteúdo completo para YouTube Gaming, incluindo roteiro estruturado e descrições profissionais de thumbnails. O projeto implementa um fluxo de trabalho com 3 agentes especializados trabalhando de forma colaborativa.

### 🎯 Objetivo
Desenvolver um sistema de IA capaz de:

1. **Pesquisar** informações atualizadas sobre jogos na web
2. **Criar roteiros** estruturados para vídeos de YouTube (8-10 minutos)
3. **Gerar descrições** de 3 opções de thumbnails profissionais
4. **Revisar e integrar** todo o conteúdo com metadados SEO otimizados

---

## 🤖 Agentes do Sistema
🎬 1. **Roteirista de Vídeo**

- **Função**: Criar roteiros estruturados e envolventes
- **Capacidades**:
-- Pesquisa de informações atualizadas sobre jogos
-- Estruturação narrativa (Introdução → Desenvolvimento → Conclusão)
Timing preciso (marcações de tempo)
CTAs estratégicos para engajamento
Linguagem adaptada ao público gamer (18-35 anos)
🎨 2. Designer de Thumbnails
Função: Criar descrições visuais de thumbnails profissionais
Capacidades:
Análise do roteiro para criar thumbnails relevantes
3 variações de design (Vibrante, Escura/Épica, Minimalista)
Prompts detalhados para geração de imagens DALL-E 3
Mockups textuais de composição visual
Recomendações baseadas em CTR esperado
✅ 3. Revisor de Conteúdo
Função: Revisar, integrar e otimizar todo o conteúdo
Capacidades:
Revisão técnica e gramatical
Integração roteiro + thumbnails
Criação de metadados SEO (título, descrição, tags)
Sugestões de melhoria
Geração do documento final integrado

---


## 🛠️ Tecnologias Utilizadas
Tecnologia	Versão	Uso
Python	3.11+	Linguagem principal
CrewAI	Latest	Framework multi-agente
OpenAI GPT	GPT-4o-mini	Modelo de linguagem
LangChain	Latest	Integração com LLMs
DuckDuckGo Search	Latest	Pesquisa web (opcional)
DALL-E 3	Latest	Geração de imagens (opcional)
Python-dotenv	Latest	Gerenciamento de variáveis

📁 Estrutura do Projeto

Nivel5Desafio/
├── agents/                      # 🤖 Agentes especializados
│   ├── __init__.py
│   ├── roteirista.py           # Agente Roteirista
│   ├── designer.py             # Agente Designer
│   └── revisor.py              # Agente Revisor
│
├── tasks/                       # 📋 Tarefas dos agentes
│   ├── __init__.py
│   ├── criar_roteiro.py        # Task de criação de roteiro
│   ├── gerar_thumbnails.py     # Task de geração de thumbnails
│   └── revisar_conteudo.py     # Task de revisão final
│
├── tools/                       # 🛠️ Ferramentas customizadas
│   ├── __init__.py
│   ├── search_tool.py          # Ferramenta de busca web
│   └── image_generator.py      # Gerador de imagens DALL-E
│
├── outputs/                     # 📂 Resultados gerados
│   ├── roteiros/               # Roteiros de vídeos
│   │   ├── .gitkeep
│   │   └── README.md
│   ├── thumbnails/             # Thumbnails e descrições
│   │   ├── images/             # Imagens PNG geradas
│   │   ├── .gitkeep
│   │   └── README.md
│   ├── .gitignore
│   └── README.md
│
├── .env.example                 # Exemplo de variáveis de ambiente
├── .gitignore                   # Arquivos ignorados pelo Git
├── main.py                      # 🚀 Ponto de entrada
├── requirements.txt             # Dependências Python
└── README.md                    # Documentação do projeto

🚀 Como Executar
1️⃣ Clonar o Repositório

git clone -b Nivel5Desafio https://github.com/ricardocr18/rocketseatCurso_IAparaDevs.git Nivel5Desafio
cd Nivel5Desafio

2️⃣ Criar Ambiente Virtual
python -m venv .venv

Ativar no Windows:
.venv\Scripts\activate

Ativar no Linux/Mac:
source .venv/bin/activate

3️⃣ Instalar Dependências
pip install -r requirements.txt

4️⃣ Configurar Variáveis de Ambiente
Copie o arquivo .env.example para .env:
cp .env.example .env

5️⃣ Executar o Sistema
python main.py

👨‍💻 Autor
Ricardo Ribeiro

⭐ Se este projeto foi útil, deixe uma estrela no repositório! ⭐
