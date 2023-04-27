from pydantic import BaseModel

class Predator(BaseModel):
    scientific_name: str
    common_name: str
    prey: str