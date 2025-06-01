from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional , Literal
load_dotenv()
import os
from pydantic import BaseModel, Field 

# importing model insitialization from langchain_openai
model = ChatOpenAI(
    model = 'openai/gpt-4.1-nano',
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Adding dynamic command base  prompt conditionby adding annotated function , now replacing the typedict parser into pydantic model parser format
class review(BaseModel):
    key_theme : list[str] = Field(description="What are the key themes in the review? List them in bullet points.")
    
    summary : str  = Field(description="A brief summary of review ")
    
    battery : Optional[str] = Field(default = None, description="what is the battery life of the product? found in the review")
    
    screen : Optional[str] = Field(default= None , description="what is the bdetail mentioned about the screen? found in the review")
    sentiment : Literal["Positive" ,"Negative"] = Field(description="Give a sentiment analysis of the review, either positive, negative, or neutral.")
    
    cons :Optional[list[str]] = Field(defualt = None , description="What are the cons of the product? if availble then give otherwise None")
    pros : Optional[list[str]] = Field(default = None , description = "What are the pros of the product? List them in bullet points.")
    name  : Optional[str] = Field(default = None , description = "Name of the Reviewer, if available in the review text, otherwise None")

structured_model = model.with_structured_output(review)


result = structured_model.invoke("""I've been using the iPhone 16 Pro Max for over a month, and I'm blown away by its sheer performance, stunning display, and revolutionary camera capabilities. Apple has truly outdone themselves with this flagship device.

*Pros:*

1. *Breathtaking Display*: The 6.9-inch Super Retina XDR display is mesmerizing, with vibrant colors and an immersive viewing experience.
2. *Camera Revolution*: The 48MP Pro camera system is incredible, capturing life-like images with ease. Night mode portraits and advanced features take mobile photography to new heights.
3. *Lightning-Fast Performance*: The A18 Pro chip delivers seamless multitasking, graphics-intensive gaming, and effortless navigation.
4. *All-Day Battery Life*: With up to 33 hours of video playback, I no longer worry about running out of juice.
5. *Sleek Design*: The titanium build and textured matte glass back exude premium quality and durability.

*Additional Highlights:*

- Dynamic Island and Always-On display provide an intuitive experience
- ProMotion technology with adaptive refresh rates up to 120Hz ensures silky-smooth visuals
- Fast charging and wireless charging (MagSafe and Qi) make powering up convenient
- IP68 rating ensures peace of mind against accidental water exposure

*Verdict:*

The iPhone 16 Pro Max is an exceptional device that justifies its premium price. If you're seeking the best iPhone experience, look no further. Apple's attention to detail, innovative features, and commitment to quality make this device a game-changer.

*Rating Breakdown:*

- Display: 5/5
- Camera: 5/5
- Performance: 5/5
- Battery Life: 5/5
- Design: 5/5
- Value: 4.5/5

*Recommendation:*

If you're due for an upgrade or seeking the ultimate smartphone experience, the iPhone 16 Pro Max is the perfect choice.
68 people found this helpful :- Priyanshu Kumar Choubey
""")



print(result)
print(result.model_dump_json(indent = 2))


