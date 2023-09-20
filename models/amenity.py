#!/usr/bin/python3

"""this has the amenity module """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ the amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # if storage_type == 'db':
    #     place_amenities = relationship("Place", secondary="place_amenity")
    # else:
    #     name = ""
