from fastapi import FastAPI

from src.api.routes import graph_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Projeto Nível 3 API",
        version="1.0.0",
        description="API para Soluções IA Agents utilizando LangGraph",
    )

    app.include_router(graph_router)


    return app

app = create_app()