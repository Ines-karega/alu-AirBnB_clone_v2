#!/usr/bin/python3
"""This module defines the State class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """Represents a State."""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """Return list of City instances with state_id equals to current State.id"""
            from models import storage
            from models.city import City
            return [city for city in storage.all(City).values() if city.state_id == self.id]
