from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional
load_dotenv()
import os


# importing model insitialization from langchain_openai
model = ChatOpenAI(
    model = 'openai/gpt-4.1-nano',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Adding dynamic command base  prompt conditionby adding annotated function
class review(TypedDict):
    key_theme : Annotated[list[str] , "What are the key themes in the review? List them in bullet points."]
    summary : Annotated[str , "A brief summary of review "]
    sentiment : Annotated[str , "Give a sentiment analysis of the review, either positive, negative, or neutral."]
    
    pros : Annotated[Optional[list[str]] , "What are the pros of the product? List them in bullet points."]

structured_model = model.with_structured_output(review)


result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
Review by Nitish Singh
""")




print(result)
print("--------------------------")
print(result["summary"])
