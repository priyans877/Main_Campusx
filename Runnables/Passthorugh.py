from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template = "Generate a joke on this topic :- {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = "Give me a explaination of this joke what it is :- {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()


# Joke Generater Chain
joke_gen = RunnableSequence(prompt1 , chatai , parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence( prompt2, chatai, parser)
})


final_chain = RunnableSequence(joke_gen , parallel_chain)


result = final_chain.invoke({'topic' : "AI"})

print(result)