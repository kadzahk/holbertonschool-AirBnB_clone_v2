#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """
    Amenity inherits from Basemodel and Base
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places_amenities = relationship(
        "Place",
        secondary="place_amenity")
