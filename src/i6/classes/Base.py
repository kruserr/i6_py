import json
import pickle


class Base():
    """
        i6 Standard base class

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, first_name, last_name):
                self.first_name = first_name
                self.last_name = last_name

        print(Person('John', 'Doe'))
        '''
        {'first_name': 'John', 'last_name': 'Doe'}
        '''
        ```
    """

    def __repr__(self):
        return str(self.get_dict())

    def get_dict(self):
        return self.__dict__

    def json(self):
        return json.dumps(self.get_dict(), indent=4, default=str)

    def dumps(self):
        return pickle.dumps(self)

    def loads(self, data):
        self.__dict__ = pickle.loads(data).__dict__

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
