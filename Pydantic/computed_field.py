from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator,computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height **2),2)
        return bmi
    

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.calculate_bmi)

    print("updated")


patient_info = {
    "name": "Nitish",
    "email": "abc@hdfc.com",
    "age": 90,
    "height" : 1.45,
    "weight": 75.2,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "2353462",'emergency':'344333'}
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)

