import json


class List():
    """
        i6 Standard list class

        Example:
        ```
        class Person(i6.Base):
            def __init__(self, name):
                super().__init__()
                self.name = name

        p1 = Person('John1')
        p2 = Person('John2')
        persons = i6.List(p1, p2)

        print(persons)
        '''
        [
            {
                'name': 'John1',
                'id': 1
            },
            {
                'name': 'John2',
                'id': 2
            }
        ]
        '''
        ```
    """
    
    def __init__(self, *argv):
        self.__items = []
        for arg in argv:
            self.__items.append(arg)

        self.__index = -1

    def __str__(self):
        return json.dumps(self.get_json(), indent=4, default=str)

    def get_json(self):
        result = []
        for item in self.__items:
            result.append(item.get_json())
        return result

    def __eq__(self, other):
        if other is None:
            return False

        len_self = len(self)
        len_other = len(other)

        if len_self != len_other:
            return False
        
        for i in range(len_self):
            if self[i] != other[i]:
                return False
        
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, key):
        return self.__items[key]

    def __iter__(self):
        return ListIterator(self)

class ListIterator():
    def __init__(self, i6_list):
        self.__i6_list = i6_list
        self.__index = -1
    
    def __next__(self):
        self.__index += 1

        if self.__index == len(self.__i6_list):
            raise StopIteration
        
        return self.__i6_list[self.__index]
    