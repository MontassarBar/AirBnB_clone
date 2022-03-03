import uuid
from datetime import datetime
class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()

    def __str__(self):
        return "[{}] (<{}>) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dictionary =  self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = datetime.now().isoformat(sep='T')
        dictionary['updated_at'] = datetime.now().isoformat(sep='T')
        return dictionary
