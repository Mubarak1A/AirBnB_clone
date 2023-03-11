#!/usr/bin/python3
""" City class Module """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherits from BaseModel:

        Public class attributes:
            state_id: string - empty string (It will be the State.id)
            name: string - empty string
    """
    state_id = ""
    name = ""
