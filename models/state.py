#!/usr/bin/python3
""" this is state module """
import models
from models.base_model import BaseModel, Base
from models import storage_t
from models.city import City
import sqlalchemy
from os import getenv
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ class state"""
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
    
    def __init__(self, *args, **kwargs):
        """initializing state"""
        super().__init__(*args, **kwargs)

    
    if models.storage_t != "db":
        @property
        def cities(self):
            '''returning list of City instances with state_id
                withthe current State.id
                FileStorage  between State and City
            '''

            from models import storage
            related_cities = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
