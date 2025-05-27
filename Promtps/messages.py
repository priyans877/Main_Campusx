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


# Adding Messages , By using Simple SystemMessage, HumanMessage, and AIMessage , static messages
messages = [
    SystemMessage(content="You are a helpful assistant that provides information and answers questions to the best of your ability. You should be polite and concise in your responses."),
    HumanMessage(content="What is the capital of France?"),
]


result = model.invoke(messages)
messages.append(AIMessage(result.content))

print(messages)

