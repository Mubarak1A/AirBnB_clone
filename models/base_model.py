#!/usr/bin/python3
""" Module for class BaseModel
    that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Public instance attributes:

            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime when an
                        instance is created
            updated_at: datetime - assign with the current datetime when an
                        instance is created and it will be updated every time
                        you change your object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != __class__:
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """  print: [<class name>] (<self.id>) <self.__dict__> """
        class_name = self.__class__.__name__
        print("{} {} {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary
            containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()

        """ a key __class__ must be added to this dictionary
            with the class name of the object
        """
        new_dict[__class__] = self.__class__.__name__

        """ created_at and updated_at must be converted to string object in:
            ISO format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        """
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()

        return new_dict
