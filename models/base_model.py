#!/usr/bin/python3
"""This module defines the BaseModel class."""
import uuid
from datetime import datetime
try:
    from sqlalchemy.orm import declarative_base
except ImportError:
    from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    if isinstance(value, str):
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        from models import storage
        storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance."""
        d = {k: v for k, v in self.__dict__.items()
             if k != '_sa_instance_state'}
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = type(self).__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in result:
            del result["_sa_instance_state"]
        return result

    def delete(self):
        """Delete currents instance from storage."""
        from models import storage
        storage.delete(self)
