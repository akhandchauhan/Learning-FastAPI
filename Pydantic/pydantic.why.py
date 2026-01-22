from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    #name: str = Field(max_length = 50)
    name: Annotated[str, Field(max_length = 50, title ='Name of the patient', description ='Given the name of patient', example = ['Nitish','Amit'])]
    age: int = Field(gt = 0, lt = 120)
    email: EmailStr 
    #weight: Optional[float] = None # default value
    #weight: float = Field(gt = 0) # greater than 0
    weight: Annotated[float, Field(gt = 0, strict = True)]
    # married: bool
    married: Annotated[bool, Field(default = None, description='Is the patient married or not')]
    linkedin : AnyUrl
    allergies: Optional[List[str]] = None
    contact_details : Dict[str, str]

def insert_patient_date(patient : Patient):

    print(patient.name) 
    print(patient.age)
    print('inserted')


patient_info = {'name':'nitish', 'age':30, 'weight' : 75.2, 'email':'abc@gmail.com', 'married': True, 'allergies': ['pollen','dust'], 'contact_details' :{'email':'abc@gmailcom', 'phone' :  '34536'}}

patient1 = Patient(**patient_info)

insert_patient_date(patient1)