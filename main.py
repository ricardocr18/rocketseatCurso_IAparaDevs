import os
from datetime import datetime
from crewai import Crew, Process
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Importar agentes
from agents.roteirista import criar_agente_roteirista
from agents.designer import criar_agente_designer
from agents.revisor import criar_agente_revisor

# Importar tasks
from tasks.criar_roteiro import criar_task_roteiro
from tasks.gerar_thumbnails import criar_task_thumbnails
from tasks.revisar_conteudo import criar_task_revisar

load_dotenv()


def main():
    """Sistema automatizado de criação de conteúdo para YouTube Gaming."""
    print("\n" + "="*80)
    print("🎮 SISTEMA DE CRIAÇÃO DE CONTEÚDO PARA YOUTUBE GAMING")
    print("="*80 + "\n")
    
    # Input do usuário
    tema = input("Digite o tema do vídeo (ex: 'Melhores jogos de 2020'): ")
    
    if not tema.strip():
        tema = "Melhores jogos de 2020"
        print(f"⚠️ Usando tema padrão: {tema}")
    
    print(f"\n🔍 Tema escolhido: {tema}")
    print(f"⏰ Iniciando em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    
    # ==================== CONFIGURAR LLM ====================
    print("🧠 Configurando LLM (OpenAI)...")
    
    llm = ChatOpenAI(
        model=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    
    print(f"✅ LLM configurado: {os.getenv('MODEL_NAME', 'gpt-4o-mini')}\n")
    
    # ==================== CRIAR AGENTES ====================
    print("🤖 Criando agentes...")
    
    roteirista = criar_agente_roteirista(llm)
    designer = criar_agente_designer(llm)
    revisor = criar_agente_revisor(llm)
    
    print("✅ Agentes criados: Roteirista, Designer, Revisor\n")
    
    # ==================== CRIAR TASKS ====================
    print("📋 Configurando tarefas...")
    
    roteiro_task = criar_task_roteiro(roteirista, tema)
    thumbnails_task = criar_task_thumbnails(designer, roteiro_task)
    revisar_task = criar_task_revisar(revisor, roteiro_task, thumbnails_task)
    
    print("✅ Tarefas configuradas: Roteiro → Thumbnails → Revisão\n")
    
    # ==================== CRIAR CREW ====================
    print("🚀 Montando equipe (Crew)...")
    
    crew = Crew(
        agents=[roteirista, designer, revisor],
        tasks=[roteiro_task, thumbnails_task, revisar_task],
        verbose=True,
        process=Process.sequential,
        max_rpm=10
    )
    
    print("✅ Crew configurado\n")
    
    # ==================== EXECUTAR ====================
    print("="*80)
    print("⚡ INICIANDO EXECUÇÃO")
    print("="*80 + "\n")
    
    try:
        resultado = crew.kickoff(inputs={'query': tema})
        
        print("\n" + "="*80)
        print("✅ EXECUÇÃO CONCLUÍDA!")
        print("="*80 + "\n")
        
        print("📄 RESULTADO FINAL:\n")
        print(resultado)
        
        # Salvar resultado
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"outputs/resultado_completo_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Resultado Completo - {tema}\n\n")
            f.write(f"**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
            f.write("---\n\n")
            f.write(str(resultado))
        
        print(f"\n💾 Resultado salvo em: {filename}")
        
    except Exception as e:
        print("\n" + "="*80)
        print("❌ ERRO")
        print("="*80)
        print(f"\n{str(e)}\n")
        raise
    
    finally:
        print("\n" + "="*80)
        print(f"⏰ Finalizado em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("="*80 + "\n")


if __name__ == "__main__":
    main()