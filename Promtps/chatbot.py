from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
import os
load_dotenv()


model = ChatOpenAI(
    model = 'qwen/qwen3-30b-a3b:free',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information and answers questions to the best of your ability. You should be polite and concise in your responses."),
]

while True:
    user_input = input("You : ")
    if user_input.lower() == 'exit':
        break
    else:
        chat_history.append(HumanMessage(user_input))
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(response.content))
        print("AI : ", response.content)
print("Chat ended. :- ", chat_history)
        
    