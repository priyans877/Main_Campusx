from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

chat_history = []
# Chat prompt template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are an helpfull customer support agent."),
        MessagesPlaceholder(variable_name= 'chat_history'),
        ("human", "{query}"),
    ]
)

# Load Chat_history
with open("C:/Users/pk877/Desktop/langchain/Main_Campusx/Promtps/chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())
    
chat_model = chat_template.invoke({ "chat_history" : chat_history , "query" : "Where is my refund"})

print(chat_model)