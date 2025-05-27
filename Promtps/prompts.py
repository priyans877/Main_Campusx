from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate , load_prompt
import streamlit as st 
from dotenv import load_dotenv
import os 
load_dotenv()


st.title("Research Paper Chatbot")
st.header("Chat with research paper")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


model = ChatOpenAI(
    model = 'qwen/qwen3-30b-a3b:free',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

template = load_prompt('template.json')


# user_input = st.text_input("Enter your question about the research paper:")

if st.button("Summarize"):
    prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input,
    }) 
    chain = template | model 
    
    responce = chain.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input,
    })
    st.write(responce.content)

