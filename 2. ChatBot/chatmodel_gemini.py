from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()


llm = ChatOpenAI(model = 'google/gemini-2.5-pro-preview' , temperature=0.7 , max_tokens=150,
    base_url= "https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    )

responce = llm.invoke("what you know about narendra modi")

print(responce.content)  # Print the response content