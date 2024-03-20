#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    place = relationship("Place", backref="cities", cascade="all, delete-orphan")

    def __init__(self, *rgs, **kwargs):
        """initializes class city"""
        super().__init__(*args, **kwargs)
