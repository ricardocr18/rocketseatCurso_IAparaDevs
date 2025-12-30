from crewai import Task

def criar_task_thumbnails(designer, roteiro_task) -> Task:
    """
    Task para gerar 3 opções de thumbnails profissionais.
    
    Args:
        designer: Agente Designer de Thumbnails
        roteiro_task: Task anterior (roteiro) para contexto
    
    Returns:
        Task configurada
    """
    return Task(
        description="""Com base no roteiro criado, gere 3 opções de thumbnails 
        profissionais para o vídeo no YouTube.
        
        **Especificações técnicas:**
        - Dimensões: 1280x720 pixels (16:9)
        - Formato: PNG ou JPG
        - Peso máximo: 2MB
        - Texto: Grande, legível, com contraste
        - Alta resolução para destaque no feed
        
        **Cada thumbnail deve ter:**
        
        1. **OPÇÃO 1 - VIBRANTE E ENERGÉTICA**
           - Cores saturadas e chamativas (vermelho, amarelo, azul vibrante)
           - Fundo gradiente ou sólido com alto contraste
           - Personagem/elemento principal em destaque (70% da área)
           - Texto com sombra/contorno grosso para legibilidade
           - Expressão facial intensa ou ação dinâmica
           - Elementos gráficos adicionais (setas, círculos, estrelas)
        
        2. **OPÇÃO 2 - ESCURA/ÉPICA**
           - Paleta de cores escuras (preto, azul escuro, roxo)
           - Iluminação dramática (luz focal no personagem)
           - Atmosfera cinematográfica e imersiva
           - Texto em branco/dourado com efeito brilho
           - Fundo desfocado ou com partículas
           - Estilo épico/sério para jogos AAA
        
        3. **OPÇÃO 3 - MINIMALISTA/PROFISSIONAL**
           - Design limpo e organizado
           - Cores sólidas ou gradiente suave
           - Tipografia moderna e legível
           - Espaço negativo estratégico
           - Foco na composição equilibrada
           - Ícones vetoriais ou símbolos relevantes
        
        **Elementos obrigatórios em TODAS as opções:**
        - Logo ou marca d'água do canal (canto superior direito)
        - Título curto e impactante (máx. 5 palavras)
        - Elemento visual principal relacionado ao jogo
        - Contraste mínimo 4.5:1 (WCAG AA)
        
        **Diretrizes de Texto:**
        - Fonte: Sans-serif, bold, tamanho 80-120pt
        - Máximo 2 linhas de texto
        - Evitar palavras genéricas ("Vídeo", "Gameplay")
        - Usar verbos de ação ou números ("TOP 5", "DESTRUINDO")
        
        **Inspiração visual:**
        - Analisar thumbnails de canais top (GameSpot, IGN, MKIceAndFire)
        - Aplicar regra dos terços na composição
        - Usar teoria das cores para emoções (vermelho=urgência, azul=confiança)
        
        **Formato de saída:**
        Para cada opção, gere:
        1. Descrição textual detalhada (prompt DALL-E)
        2. URL da imagem gerada
        3. Justificativa da escolha visual
        4. Score de clickability (0-10)
        
        Exemplo de formato:
        ```
        ## OPÇÃO 1: Vibrante
        **Descrição:** Thumbnail com fundo gradiente vermelho-laranja, personagem 
        do jogo em pose dinâmica ocupando 70% da área, texto "TOP 10 JOGOS 2020" 
        em fonte Impact branca com contorno preto de 5px, logo do canal no canto 
        superior direito.
        
        **Prompt DALL-E:** "YouTube thumbnail, vibrant red-orange gradient background, 
        dynamic video game character in action pose, large bold white text 'TOP 10 
        GAMES 2020', black outline, professional gaming channel aesthetic, 1280x720px"
        
        **URL:** [URL da imagem gerada]
        
        **Justificativa:** Cores quentes geram urgência e chamam atenção. 
        Personagem em ação cria expectativa de conteúdo dinâmico.
        
        **Clickability Score:** 9/10
        ```
        
        Repita para as 3 opções e recomende qual usar baseado em:
        - Algoritmo do YouTube (CTR esperado)
        - Público-alvo do vídeo
        - Tendências atuais de design""",
        
        expected_output="""Um documento em Markdown contendo:
        
        # Thumbnails Geradas
        
        ## 📊 Análise do Roteiro
        - Tema principal: [extraído do roteiro]
        - Jogos mencionados: [lista]
        - Tom do vídeo: [casual/sério/humorístico]
        - Público-alvo: [idade e perfil]
        
        ## 🎨 Opção 1: Vibrante e Energética
        [Descrição completa + prompt + URL + justificativa + score]
        ![Thumbnail 1](URL_da_imagem_1)
        
        ## 🌑 Opção 2: Escura e Épica
        [Descrição completa + prompt + URL + justificativa + score]
        ![Thumbnail 2](URL_da_imagem_2)
        
        ## ✨ Opção 3: Minimalista e Profissional
        [Descrição completa + prompt + URL + justificativa + score]
        ![Thumbnail 3](URL_da_imagem_3)
        
        ## 🏆 Recomendação Final
        **Thumbnail escolhida:** Opção [X]
        
        **Motivo:**
        - CTR esperado: [X]%
        - Melhor adequação ao público: [justificativa]
        - Tendência de mercado: [análise]
        
        **Testes A/B sugeridos:**
        1. [Variação 1]
        2. [Variação 2]
        
        ## 📈 Métricas de Sucesso
        - CTR esperado: [X]%
        - Visualizações previstas (primeiro dia): [X]
        - Público-alvo alcançado: [X]%
        """,
        
        agent=designer,
        context=[roteiro_task],  # Usa o roteiro como contexto
        output_file="outputs/thumbnails/thumbnails_opcoes.md"
    )