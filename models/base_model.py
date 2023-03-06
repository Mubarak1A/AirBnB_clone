#!/bin/python3
""" Module for class BaseModel
    that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ BaseModel class """

    def __init__(self, id, created_at, updated_at):
        """ Public instance attributes:

            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime when an
                        instance is created
            updated_at: datetime - assign with the current datetime when an
                        instance is created and it will be updated every time
                        you change your object
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """  print: [<class name>] (<self.id>) <self.__dict__> """

        class_name = self.__class__.__name__
        print("{} {} {}".format(class_name, self.id, self.__dict__))


test = BaseModel(str(uuid4()), datetime.utcnow(), datetime.utcnow())
test.__str__()
