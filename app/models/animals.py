from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    scientific_name = Column(String)
    popular_name = Column(String)

    relationships = relationship("Relationship", back_populates="animal")

class Relationship(Base):
    __tablename__ = "relationships"

    predator_id = Column(Integer, ForeignKey("animals.id"), primary_key=True)
    prey_id = Column(Integer, ForeignKey("animals.id"), primary_key=True)
    weight = Column(Integer)
    animal = relationship("Animal", back_populates="relationships")
