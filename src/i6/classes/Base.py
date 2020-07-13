import json
import pickle


class Base():
    """
        i6 Standard base class

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, name):
                self.name = name

        print(Person('John'))
        '''
        {'name': 'John'}
        '''
        ```
    """

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def json(self):
        """
            Returns a valid json representation of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            print(Person('John').json())

            '''
            {
                "name": "John"
            }
            '''
            ```
        """

        return json.dumps(self.__dict__, indent=4, default=str)

    def load_json(self, data):
        """
            Load data from json.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            p1 = Person('John1')
            p2 = Person('John2')

            p2.load_json(p1.json())
            print(p2)
            '''
            {'name': 'John1'}
            '''
            ```
        """

        self.__dict__ = json.loads(data)

    def serialize(self):
        """
            Returns a binary serialization of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            with open('person.pkl', 'wb') as f:
                f.write(Person('John').serialize())
            ```
        """

        return pickle.dumps(self)

    def deserialize(self, data):
        """
            Deserialize a valid binary serialization of the class.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            person = Person('Doe')

            with open('person.pkl', 'rb') as f:
                person.deserialize(f.read())

            print(person)
            '''
            {'name': 'John'}
            '''
            ```
        """

        self.__dict__ = pickle.loads(data).__dict__
