from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough , RunnableLambda , RunnableBranch
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

report_gen = RunnableSequence(prompt1, chatai, parser) 

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 200  , RunnableSequence(prompt2 , chatai , parser)),
    RunnablePassthrough(),
    #RunnableLambda(lambda x: "Your Co ntent Limit Exceeds {}".format(len(x.split())))
)

final_chain = RunnableSequence(
    report_gen,
    branch_chain
)

result = final_chain.invoke({'topic': 'AI in 2025: Trends and Predictions In 200 words'})

print(result)