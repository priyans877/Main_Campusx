from pydantic import BaseModel, Field
from typing import TypedDict, Optional

class User(BaseModel):
    
    name : str = "Priyanshu"
    age : Optional[int] = None
    Cgpa : float = Field(gt = 0 , lt =10  , defualt = 5 , discription = "A CGPAvalue which tend the score of a student into his full time counrse")
    
    
    
user_dic = {"name": "Priyanshu", "age": 20, "Cgpa": 9.5}

student = User(**user_dic)
 
student_dict  = dict(student)

json_output = student.model_dump_json(indent = 2)
print(json_output)