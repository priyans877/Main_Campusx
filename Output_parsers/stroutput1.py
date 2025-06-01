from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain_core.output_parsers import StrOutputParser   
import os

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = ChatOpenAI(
    model = 'openai/gpt-4.1-nano',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)   


# model = ChatHuggingFace(llm=llm)

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


# prompt1 = template1.invoke({"input" : "Artificial Intelligence in Healthcare"})

parser = StrOutputParser()

chain = template1 | llm | parser | template2 | llm | parser


result = chain.invoke({"input": "Artificial Intelligence in Healthcare"})
print(result)