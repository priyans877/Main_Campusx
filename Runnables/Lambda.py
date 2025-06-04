from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough , RunnableLambda
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template = "Generate Linkedin Professional post on this topic :- {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate Tweet regarding this topic and its hype In 2025 :- {topic}",
    input_variables= ['topic']
)

parser = StrOutputParser()


def word_count(text):
    return len(text.split())

joke_gen = RunnableSequence(prompt1 , chatai , parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count' : RunnableLambda(word_count),
    'explaination': RunnableSequence( prompt2, chatai, parser)
})


final_chain = RunnableSequence(joke_gen , parallel_chain)


result = final_chain.invoke({'topic' : "AI"})

print(result)
