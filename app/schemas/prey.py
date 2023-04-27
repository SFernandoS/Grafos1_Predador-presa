from pydantic import BaseModel

class Prey(BaseModel):
    scientific_name: str
    common_name: str
    prey: str