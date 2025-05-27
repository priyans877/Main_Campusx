from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import pandas as pd
import os
import json
import re

# Get The Current Script Directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "cleaned_output.csv")

# Load the CSV
df = pd.read_csv(file_path)

# Defining Chat Model With OpenRouterAPI Key
chat = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1", 
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="mistralai/mistral-7b-instruct",
    max_completion_tokens=100
)

# I am using LangChain for generating Human Friendly Personalized Messages for Every Attendies
def generate_llm_message(row):
    name = row['name']
    job_title = row['Job Title']
    has_joined = row['has_joined_event']
    
    event_status = "joined" if has_joined else "did not join"
    # prompt = f"""
    #     You are an expert marketing assistant writing short, friendly LinkedIn-style follow-up messages.

    #     Write a warm, personalized message for a professional named {name} dont make mistake on naming ,and prevent blank "Your name" type mistake, who works as a {job_title}.
    #     They **{event_status}** the recent event.

    #     🎯 Guidelines:
    #     - Use the person’s name naturally.
    #     - If they {event_status}, thank them and invite them to try something related to their field.
    #     - If they **missed it**, mention their job title and say another session is being planned just for people like them.
    #     - Keep the message casual and no longer than 50 words.
    #     - Add one relevant emoji inline (🎉, 🙌, 💡, etc.).
    #     - Don’t include a subject or greeting.
    #     - If referring to the next event, describe it based on the {job_title}. Example: "AI tools for designers", "Product strategy workshop", etc.
    #     - Don't do silly spelling word mistakes.
    #     - Dont add Best regard or name anything about sender.

    #     Now write the message.
    #     """
        
    prompt = f"""
        You are an expert marketing assistant writing **short, friendly LinkedIn-style follow-up messages**.

        ✍️ Write a warm, customized message for:
        - Start Hey Name: {name}
        - Job Title: {job_title}
        - Event Status: {event_status}

        💡 Rules:
        - Do NOT include greetings (Hi, Hello) or sign-offs (Regards, Best, Your Name, etc.)
        - Do NOT write "Looking forward to..." or similar endings.
        - Just the core message — finish the message naturally, no closing lines.
        - Add one relevant emoji inline (🎉, 🙌, 💡, etc.)
        - Must be **under 40 words**
        - Focus on what they'd care about (like future sessions for their role)

        🎯 Examples:
        - For Joined: Thanks for joining! As a {job_title}, you’ll love our next AI tools session 🎉
        - For Missed: Sorry we missed you 🙈! We’re planning a new event for {job_title}s — want a heads-up?

        Now write the message.
        """

    
    messages = [
        SystemMessage(content="You are an expert marketing assistant writing personalized follow-up messages."),
        HumanMessage(content=prompt)
    ]
    
    response = chat.invoke(messages)
    formated_r = re.sub(r'\n+', '\n', response.content.strip())
    print(response.content)
    print("--------------------------------------------------------------------")
    return formated_r

# Generate Messages
df['message'] = df.apply(generate_llm_message, axis=1)

# Save Messages
print("I am Here")
df[['email', 'message']].to_csv("personalized_messages.csv", index=False)

#
os.makedirs("llm_user_messages", exist_ok=True)
for _, row in df.iterrows():
    email = row['email']
    msg = row['message']
    
    with open(f"personalized_msg.json", "a", encoding='utf-8') as f:
        json.dump({"email": row['email'], "message": msg}, f, indent=4)

print("Generated messages saved.")
