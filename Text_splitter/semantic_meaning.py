from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
import os

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)


sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_amount=1 , 
    breakpoint_threshold_type="standard_deviation",  # 1 for 'amount', 2 for 'percentage'
)

chunk = splitter.create_documents([sample])

print(len(chunk))
print(chunk)