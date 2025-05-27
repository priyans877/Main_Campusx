from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id= "HuggingFaceH4/zephyr-7b-beta",
    task = 'text-generation',
    # huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    pipeline_kwargs= dict(
        temperature = 0.7,
        max_new_tokens = 150,
    )
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("Explain me chain Derivation methos in Mathmatics?")

print(result.content)  # Print the response content

