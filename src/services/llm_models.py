from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
import httpx
 
load_dotenv()
 
httpx_client = httpx.Client(verify=False)
 
llm_4o_mini = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    http_client=httpx_client,       
)