from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
import os

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
 
    task = 'text-generation',
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm = llm)


schema = [
    ResponseSchema(name = "fact_1" , description = "First fact about the topic"),
    ResponseSchema(name = "fact_2" , description = "Second fact about the topic"),
    ResponseSchema(name = "fact_3" , description = "Third fact about the topic"),
]
parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template = "give me a 3 fact about topic {topic} \n {Parser_formation}",
    input_variables= ["topic"],
    partial_variables={"Parser_formation" : parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic" : "Black Hole"})
 
print(result)