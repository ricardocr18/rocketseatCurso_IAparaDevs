from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = Chroma.from_documents(chunks, embedding=embeddings, persist_directory="vector_db")
    return vectorstore

def get_vectorstore():
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = Chroma(persist_directory="vector_db", embedding_function=embeddings)
    return vectorstore