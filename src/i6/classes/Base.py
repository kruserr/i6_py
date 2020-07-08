import json


class Base():
    """
        i6 Standard base class

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, name):
                super().__init__()
                self.name = name

        print(Person('John'))
        '''
        {
            'id': 1,
            'name': 'John',
        }
        '''
        ```
    """
    
    __ID_COUNTER = 0

    def __init__(self):
        self.__id = Base.__auto_id()

    def __str__(self):
        return json.dumps(self.get_json(), indent=4, default=str)

    def get_json(self):
        temp_dict = self.__dict__.copy()
        temp_dict['id'] = temp_dict.pop(f"_{__class__.__name__}__id")
        return temp_dict

    def __eq__(self, other):
        if other is None:
            return False
        return self.get_id() == other.get_id()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __auto_id():
        Base.__ID_COUNTER += 1
        return Base.__ID_COUNTER

    def get_id(self):
        return self.__id
    