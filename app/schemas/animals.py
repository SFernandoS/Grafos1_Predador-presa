from pydantic import BaseModel

class AnimalCreate(BaseModel):
    id: int
    scientific_name: str
    popular_name: str

    class Config:
        orm_mode = True


class RelationshipCreate(BaseModel):
    predator: AnimalCreate
    prey: AnimalCreate
    weight: int

    class Config:
        orm_mode = True
