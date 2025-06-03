from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()


model = ChatOpenAI(
    model = 'openai/gpt-4.1-nano',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Generate 5 interesing Fact about : - {topic}",
    input_variables= ["topic"]
)


chain = prompt | model | parser


result = chain.invoke({'topic': 'Python programming language'})
print(result)


chain.get_graph().print_ascii()
