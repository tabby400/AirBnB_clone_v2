#!/usr/bin/python3
""" this is state module """

from models.base_model import BaseModel, Base
from models import storage_t
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ class state"""

    __tablename__ = 'states'
    if storage_t == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

    if models.storage_t != "db":

        @property
        def cities(self):
            '''returning list of City instances with state_id
                withthe current State.id
                FileStorage  between State and City
            '''

            from models import storage
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
