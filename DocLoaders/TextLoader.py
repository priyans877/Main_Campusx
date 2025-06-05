from model import chatai
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate



text_load = TextLoader("cricket.txt", encoding="utf-8")

prompt = PromptTemplate(
    template = "Write a summary from the following Poem :- {poem}",
    input_variables=["poem"],
)

chain = prompt | chatai | StrOutputParser()
# print(text_load.load())

print(type(text_load.load()))

data = text_load.load()

print(len(data))

result = chain.invoke({"poem" : data[0].page_content})


print(result)