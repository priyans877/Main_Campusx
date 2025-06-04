from chain.model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser



prompt1 = PromptTemplate(
    template = "Write a joke About this topic :- {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template = "Explain me this joke :- {joke}",
    input_variables=["content"]
)


parser = StrOutputParser()

chain  = RunnableSequence(prompt1, chatai , parser , prompt2 , chatai , parser )

result = chain.invoke({"topic": "Python programming"})

print(result)