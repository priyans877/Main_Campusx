from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()


# os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

# # Enable LangSmith tracking (optional)
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


llm = ChatOpenAI(
    model = "gpt-3.5-turbo-instruct",
    base_url= "https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),  # Use OpenRouter API key
    )

result = llm.invoke("What is the hieght of mount everest?")

print(result.content)