from typing import TypedDict

# Define a TypedDict for a person
class Person(TypedDict):
    name: str
    age: int
    email: str
    
 
new_person : Person = {'name' : 'Priyanshu'  , 'age' : 22 , 'email' : 'pchoubey030@gmail.com'}
print(new_person)