#!/usr/bin/python3
"""This module defines the Amenity class."""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Represents an Amenity."""

    __tablename__ = 'amenities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
