from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()


chatai = ChatOpenAI(
    model = 'openai/gpt-4.1-nano',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)