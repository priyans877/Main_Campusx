# from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import SequentialChain
from dotenv import load_dotenv
from pydantic import BaseModel ,Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
import os
from langchain.schema.runnable import RunnableParallel , RunnableBranch , RunnableLambda
from model import chatai
load_dotenv()

# Schema 
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')



output_parser = PydanticOutputParser(pydantic_object = Feedback)


parser = StrOutputParser()


prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following text into positive, negative, neutral: {text} \n {formation}",
    input_variables = ["text"],
    partial_variables= {'formation' : output_parser.get_format_instructions()}
)

# Prompt 2 for positive feedback response
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)
# Prompt3 For negative feedback response
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

classify_chain = prompt1 | chatai | output_parser

positive_chain = prompt2 | chatai | parser

negative_chain = prompt3 | chatai | parser

branch = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , positive_chain),
    (lambda x:x.sentiment == 'negative' , negative_chain),
    RunnableLambda(lambda x: "Thank you for your Feedback")
)

final_chain  = classify_chain | branch

result = final_chain.invoke({'text' : "I have a no issue with thsi phone and loved its new feature of camera and battery life"})


print(result)

final_chain.get_graph().print_ascii()