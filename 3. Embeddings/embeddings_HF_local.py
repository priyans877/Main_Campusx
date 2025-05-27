from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os


load_dotenv()


embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
)


documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


vector = embeddings.embed_documents(documents)

query = "Tell Me about Rohit Sharma"

query = embeddings.embed_query(query)  

score = cosine_similarity([query], vector)[0]

# print(list(enumerate(score)))
index , score = sorted(list(enumerate(score)) , key = lambda x:x[1])[-1]


print("Best Result is :- " ,documents[index])
print("Its Matching Score is :- " , score)