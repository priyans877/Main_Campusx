from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
import os
load_dotenv()


model = ChatOpenAI(
    model = 'qwen/qwen3-30b-a3b:free',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

chat_prompt = ChatPromptTemplate([
    ("system" , "You Are an Expert In {domain} domain"),
    ("human" , "Explain In simple term , what is {topic}")
])


result = chat_prompt.invoke({"domain": "Artificial Intelligence", "topic": "Generative AI"})
print(result)