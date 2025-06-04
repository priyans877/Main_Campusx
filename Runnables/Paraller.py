from model import chatai
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnableSequence
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

paraller_chain = RunnableParallel({
    'linkedin_post': RunnableSequence(prompt1 , chatai , parser),
    'tweet': RunnableSequence( prompt2, chatai ,parser)
})

result = paraller_chain.invoke({'topic' : "AI"})

print(result['linkedin_post'])
print("-------------------------------------------------------------------------------"*30)
print(result['tweet'])

