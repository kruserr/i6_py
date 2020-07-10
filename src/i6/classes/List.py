import json
import pickle


class List(list):
    """
        i6 Standard list class

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, name):
                self.name = name

        p1 = Person('John1')
        p2 = Person('John2')
        persons = i6.List(p1, p2)

        print(persons)
        '''
        [{'name': 'John1'}, {'name': 'John2'}]
        '''
        ```
    """
    
    def __init__(self, *argv):
        super().__init__(argv)

    def json(self):
        """
            Returns a valid json representation of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name
            
            p1 = Person('John1')
            p2 = Person('John2')
            persons = i6.List(p1, p2)

            print(persons.json())
            '''
            [
                {
                    "name": "John1"
                },
                {
                    "name": "John2"
                }
            ]
            '''
            ```
        """
        
        temp_items = []
        for item in self:
            temp_items.append(item.__dict__)
        return json.dumps(temp_items, indent=4, default=str)

    def dumps(self):
        """
            Returns a binary serialization of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name
            
            p1 = Person('John1')
            p2 = Person('John2')
            persons = i6.List(p1, p2)

            with open('persons.pkl', 'wb') as f:
                f.write(persons.dumps())
            ```
        """

        return pickle.dumps(self)

    def loads(self, data):
        """
            Deserialize a valid binary serialization of the list.

            Example:
            ```
            class Person(i6.Base):
                def __init__(self, name):
                    self.name = name

            persons = i6.List()

            with open('persons.pkl', 'rb') as f:
                persons.loads(f.read())

            print(persons)
            '''
            [{'name': 'John1'}, {'name': 'John2'}]
            '''
            ```
        """

        self.clear()
        for item in pickle.loads(data):
            self.append(item)
    