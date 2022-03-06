#!/usr/bin/python3
'''BaseModel class'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    Public instance attributes:
        -id: string - assign with an uuid when an instance is created.
        -created_at: datetime - assign with the current datetime when
        an instance is created.
        -updated_at: datetime - assign with the current datetime when
        an instance is created and it will be updated every time you
        change your object.
    '''
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''prints [<class name>] (<self.id>) <self.__dict__>'''
        return "[{}] (<{}>) <{}>".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute updated_at with the current
        datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of __dict__ of
        the instance'''
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = datetime.now().isoformat(sep='T')
        dictionary['updated_at'] = datetime.now().isoformat(sep='T')
        return dictionary
