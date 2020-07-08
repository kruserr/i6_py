import i6


class Person(i6.Base):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

p1 = Person('John1', 'Doe1')
p2 = Person('John2', 'Doe2')
persons = i6.List(p1, p2)
persons2 = i6.List(p1)

print(p1)
print(p2)
print(persons)
print(persons2)
for person in persons:
    print(person)

print(p1 == p1)
print(p1 != p2)
print(persons == persons)
print(persons != persons2)
