from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas.animals import AnimalCreate, RelationshipCreate
from services.graph import GraphService

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/animals/", response_model=AnimalCreate)
def create_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    return GraphService.create_animal(db, animal)

@router.post("/relationships/", response_model=RelationshipCreate)
def create_relationship(relationship: RelationshipCreate, db: Session = Depends(get_db)):
    return GraphService.create_relationship(db, relationship)

@router.get("/search/{predator}/{prey}")
def search_relationship(predator: str, prey: str, db: Session = Depends(get_db)):
    return GraphService.search_relationship(db, predator, prey)
