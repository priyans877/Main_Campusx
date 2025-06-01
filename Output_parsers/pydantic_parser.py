from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
import os
from pydantic import BaseModel , Field

load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
 
    task = 'text-generation',
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm = llm)


class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt = 18  , description="Age Of THe person")
    city: str = Field(description="City where the person lives")
    
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "Generate a name , City  , Age of person of a fictiional {place} person \n {Parser_formation}",
    input_variables= ["place"],
    partial_variables={"Parser_formation" : parser.get_format_instructions()}
)

chain = template | model | parser

print(template)
result = chain.invoke({"place" : "Indian"})

print(result)
