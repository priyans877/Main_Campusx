from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
import os

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
 
    task = 'text-generation',
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm = llm)
#template 1

template1 = PromptTemplate(
    input_variables=["input"],
    template="You are a helpful assistant. Please write report on this topic :- {input}"
)
# template 2

template2 = PromptTemplate(
    template="You are a helpful assistant. write a 5line summary about this text :- {text}",
    input_variables=["text"]
)


prompt1 = template1.invoke({"input" : "Artificial Intelligence in Healthcare"})

result = model.invoke(prompt1)

print(result.content)

print("----------------------------------------------------------------------------------------------------")
prompt2 = template2.invoke({"text" : result.content})

result1 = model.invoke(prompt2)

print(result1.content)  


