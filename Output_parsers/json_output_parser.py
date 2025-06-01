from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
 
    task = 'text-generation',
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    # You are a helpful assistant. Please write report on this topic Start Data analystics Career in Helatcare device company
    template = "give me a five fact about topic {topic} \n {Parser_formation}",
    input_variables= ["topic"],
    partial_variables={"Parser_formation": parser.get_format_instructions()}
)

# prompts = template.format()

# print(prompts)

# result = model.invoke(prompts)


# with chains

chain = template | model | parser

result = chain.invoke({"topic" : "Black Hole"})

print(result.content)
