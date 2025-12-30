"""
Ferramenta de pesquisa usando DuckDuckGo Search nativa do CrewAI.
"""

from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from duckduckgo_search import DDGS


def search_web(query: str, max_results: int = 10) -> str:
    """
    Busca informações na web usando DuckDuckGo.
    
    Args:
        query: Query de busca
        max_results: Número máximo de resultados
    
    Returns:
        String formatada com resultados
    """
    try:
        enhanced_query = f"{query} videogame gaming"
        
        with DDGS() as ddgs:
            results = list(ddgs.text(
                enhanced_query,
                region="br-pt",
                safesearch='off',
                max_results=max_results
            ))
        
        if not results:
            return f"❌ Nenhum resultado encontrado para: {query}"
        
        output = f"# 🔍 Resultados: {query}\n\n"
        
        for i, result in enumerate(results, 1):
            title = result.get('title', 'Sem título')
            snippet = result.get('body', 'Sem descrição')
            url = result.get('href', '#')
            
            if len(snippet) > 300:
                snippet = snippet[:297] + "..."
            
            output += f"## {i}. {title}\n"
            output += f"**URL:** {url}\n"
            output += f"**Resumo:** {snippet}\n\n"
        
        return output
    
    except Exception as e:
        return f"⚠️ Erro: {str(e)}"


def search_news(query: str, max_results: int = 5) -> str:
    """
    Busca notícias recentes.
    
    Args:
        query: Termo de busca
        max_results: Número de notícias
    
    Returns:
        String com notícias
    """
    try:
        with DDGS() as ddgs:
            news_results = list(ddgs.news(
                query,
                region="br-pt",
                safesearch='off',
                max_results=max_results
            ))
        
        if not news_results:
            return f"❌ Nenhuma notícia encontrada: {query}"
        
        output = f"# 📰 Notícias: {query}\n\n"
        
        for i, news in enumerate(news_results, 1):
            title = news.get('title', 'Sem título')
            date = news.get('date', 'Data desconhecida')
            source = news.get('source', 'Fonte desconhecida')
            url = news.get('url', '#')
            body = news.get('body', 'Sem conteúdo')
            
            output += f"## {i}. {title}\n"
            output += f"**Data:** {date} | **Fonte:** {source}\n"
            output += f"**URL:** {url}\n"
            output += f"{body}\n\n"
        
        return output
    
    except Exception as e:
        return f"⚠️ Erro: {str(e)}"


# Classe para compatibilidade
class SearchTool:
    """Wrapper de busca"""
    def __init__(self):
        pass
    
    def search(self, query: str) -> str:
        return search_web(query)