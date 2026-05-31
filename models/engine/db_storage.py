#!/usr/bin/python3
"""This module defines the DBStorage engine"""
import os
try:
    import MySQLdb
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        classes = (User, State, City, Amenity, Place, Review)
        obj_dict = {}

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for c in classes:
                objs.extend(self.__session.query(c).all())

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add object to current database session."""
        if obj is not None:
            try:
                self.__session.add(obj)
            except Exception:
                pass

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session."""
        self.__session.close()
