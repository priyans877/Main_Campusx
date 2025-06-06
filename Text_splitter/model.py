from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
load_dotenv()


chatai = ChatOpenAI(
    model = 'openai/gpt-4.1-nano',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",   # or text-embedding-ada-002
    api_key=os.environ["OPENAI_API_KEY"],
    base_url = "https://openrouter.ai/v1",
)