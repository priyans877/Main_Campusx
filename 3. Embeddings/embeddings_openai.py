from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os


load_dotenv()


embeddings = OpenAIEmbeddings(
    model = "openai/text-embedding-3-small",
    base_url="https://openrouter.ai/api/v1",
    api_key= os.getenv("OPENAI_API_KEY")
)

vector = embeddings.embed_query("What is the capital of France?")

print(vector)