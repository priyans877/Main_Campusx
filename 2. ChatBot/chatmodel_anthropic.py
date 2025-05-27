from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  
import os 


llm = ChatOpenAI(
    model = "anthropic/claude-opus-4",
    temperature=0.7,
    max_completion_tokens=150,
    base_url="https://openrouter.ai/api/v1",
    api_key= os.getenv("OPENAI_API_KEY"),  # Use OpenRouter API key
)

result = llm.invoke("what your method aproach for solving a real life problem as human?")
print(result.content)  # Print the response content