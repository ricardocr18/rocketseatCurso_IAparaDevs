from crewai import Task

def criar_task_revisar(revisor, roteiro_task, thumbnails_task) -> Task:
    """
    Task para revisar e integrar roteiro + thumbnails.
    
    Args:
        revisor: Agente Revisor
        roteiro_task: Task do roteiro
        thumbnails_task: Task das thumbnails
    
    Returns:
        Task configurada
    """
    return Task(
        description="""Revise o roteiro e integre as thumbnails geradas em um 
        documento final profissional.
        
        **Responsabilidades:**
        
        1. **Revisão do Roteiro:**
           - Corrigir erros ortográficos e gramaticais
           - Melhorar fluidez e coesão textual
           - Verificar estrutura narrativa (introdução, desenvolvimento, conclusão)
           - Ajustar tom e linguagem para o público-alvo
           - Garantir timing adequado (1 minuto de vídeo ≈ 150 palavras)
        
        2. **Otimização para YouTube:**
           - Adicionar marcadores de tempo (timestamps)
           - Inserir calls-to-action estratégicos
           - Sugerir momentos para ganchos de retenção
           - Indicar pontos para cortes de edição
        
        3. **Integração de Thumbnails:**
           - Avaliar cada thumbnail em relação ao roteiro
           - Escolher a thumbnail mais adequada
           - Justificar a escolha baseado em métricas
           - Sugerir variações para testes A/B
        
        4. **Documento Final:**
           - Formatar em Markdown profissional
           - Incluir metadados do vídeo (título, descrição, tags)
           - Adicionar seção de SEO para YouTube
           - Incorporar as 3 thumbnails geradas
        
        **Checklist de Qualidade:**
        - [ ] Roteiro segue estrutura narrativa clara
        - [ ] Texto revisado (0 erros ortográficos)
        - [ ] Tom adequado ao público-alvo
        - [ ] Timestamps adicionados
        - [ ] Calls-to-action inseridos
        - [ ] Thumbnail recomendada justificada
        - [ ] Metadados SEO incluídos
        - [ ] Formato Markdown válido""",
        
        expected_output="""Um documento final em Markdown contendo:
        
        # 🎬 Roteiro Completo: [Título do Vídeo]
        
        ## 📋 Metadados do Vídeo
        
        **Título:** [título otimizado SEO, máx. 70 caracteres]
        **Descrição:** [descrição completa, 300-500 palavras]
        **Tags:** [15-20 tags relevantes]
        **Categoria:** Gaming
        **Público:** [idade e perfil]
        **Duração estimada:** [X] minutos
        
        ---
        
        ## 📝 Roteiro (Versão Revisada)
        
        ### [00:00-00:15] Introdução
        [texto do roteiro revisado]
        
        **📍 CTA:** Não esqueça de dar like e se inscrever!
        
        ### [00:15-01:30] Tema Principal
        [texto do roteiro revisado]
        
        **✂️ Corte sugerido:** Transição para gameplay
        
        ### [01:30-02:00] Conclusão
        [texto do roteiro revisado]
        
        **📍 CTA:** Comente seu jogo favorito de 2020!
        
        ---
        
        ## 🎨 Thumbnails Geradas
        
        ### Opção 1: Vibrante
        ![Thumbnail 1](URL)
        **Score:** 9/10
        
        ### Opção 2: Escura
        ![Thumbnail 2](URL)
        **Score:** 8/10
        
        ### Opção 3: Minimalista
        ![Thumbnail 3](URL)
        **Score:** 7/10
        
        ---
        
        ## 🏆 Thumbnail Recomendada
        
        **Escolhida:** Opção 1 (Vibrante)
        
        **Justificativa:**
        - Maior CTR esperado (12-15%)
        - Cores quentes atraem mais cliques
        - Adequada ao público jovem (18-34 anos)
        - Segue tendências de canais top
        
        ---
        
        ## 🔍 Otimização SEO
        
        **Palavras-chave primárias:**
        - Melhores jogos 2020
        - Top games 2020
        - Jogos do ano 2020
        
        **Palavras-chave secundárias:**
        - Animal Crossing New Horizons
        - Hades gameplay
        - The Last of Us Part II análise
        
        **Concorrência:** Média
        **Volume de busca:** Alto (50K-100K/mês)
        
        ---
        
        ## 📊 Métricas Esperadas
        
        - **Visualizações (24h):** 5.000-10.000
        - **CTR:** 12-15%
        - **Retenção média:** 60-70%
        - **Engajamento:** 8-10% (likes + comentários)
        
        ---
        
        ## ✅ Status Final
        
        - [x] Roteiro revisado
        - [x] Thumbnails geradas
        - [x] Metadados otimizados
        - [x] SEO configurado
        - [x] Pronto para produção
        
        **Data de criação:** [data atual]
        **Versão:** 1.0
        """,
        
        agent=revisor,
        context=[roteiro_task, thumbnails_task],
        output_file="outputs/roteiro_final.md"
    )