from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from src.services.llm_models import llm_4o_mini
from src.nodes.agent.rag.vectorstore import get_vectorstore

def get_rag_chain():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()
    prompt = ChatPromptTemplate.from_template(
        "Responda de forma clara e objetiva: {question}\nContexto: {context}"
    )
    setup = RunnableParallel({
        "question": lambda x: x["question"],
        "context": lambda x: retriever.invoke(x["question"])
    })

    def join_context(inputs):
        context = inputs["context"]
        if isinstance(context, list):
            return {
                "question": inputs["question"],
                "context": "\n".join(doc.page_content for doc in context)
            }
        return inputs

    chain = setup | join_context | prompt | llm_4o_mini
    return chain