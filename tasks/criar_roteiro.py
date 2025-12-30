from crewai import Task
from datetime import datetime

def criar_task_roteiro(roteirista, query: str) -> Task:
    """
    Task para criar roteiro de vídeo sobre games.
    """
    return Task(
        description=f"""Pesquise e crie um roteiro completo para um vídeo no YouTube 
        sobre o tema: "{query}".
        
        O roteiro deve conter:
        
        1. **TÍTULO DO VÍDEO** (otimizado para SEO)
           - Máximo 60 caracteres
           - Inclua palavras-chave relevantes
        
        2. **INTRODUÇÃO** (primeiros 15 segundos)
           - Hook para prender a atenção
           - Apresentação do tema
           - Promessa de valor
        
        3. **DESENVOLVIMENTO** (corpo principal)
           - Liste os jogos/tópicos principais (3-5 itens)
           - Para cada item, inclua:
             * Nome do jogo
             * Principais características
             * Por que merece destaque
             * Curiosidades ou fatos interessantes
        
        4. **CONCLUSÃO** (últimos 30 segundos)
           - Resumo dos pontos principais
           - Call-to-action (CTA)
           - Convite para like, comentário e inscrição
        
        5. **ELEMENTOS VISUAIS SUGERIDOS**
           - Descrição de cenas-chave para b-roll
           - Momentos que merecem destaque visual
        
        Data atual: {datetime.now().strftime('%d/%m/%Y')}
        
        Use a ferramenta de pesquisa para buscar informações atualizadas.""",
        
        expected_output="""Um roteiro completo em formato Markdown com:
        
        # [TÍTULO DO VÍDEO]
        
        ## 📊 Informações do Vídeo
        - **Duração estimada:** X minutos
        - **Público-alvo:** [descrição]
        - **Palavras-chave:** tag1, tag2, tag3
        
        ## 🎬 ROTEIRO
        
        ### Introdução (0:00 - 0:15)
        [Texto do narrador]
        
        ### Desenvolvimento
        
        #### 1. [Nome do Jogo/Tópico 1]
        **Timestamp:** 0:15 - X:XX
        [Conteúdo detalhado]
        
        [Repetir para cada tópico]
        
        ### Conclusão (X:XX - Final)
        [Texto do narrador]
        
        ## 🎨 Elementos Visuais Sugeridos
        - [Descrição de cenas]
        
        ## 📝 Notas de Produção
        - [Observações importantes]
        """,
        
        agent=roteirista
    )