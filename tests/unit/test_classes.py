import i6


class Person(i6.Base):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

p1 = Person('John1', 'Doe1')
p2 = Person('John2', 'Doe2')
persons = i6.List(p1, p2)
persons2 = i6.List(p1)

print(persons)

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

print(p1.json())
print(p2.json())
print(persons.json())
print(persons2.json())

print(p1)

persons2.deserialize(persons.serialize())
print(persons2)

print(p2)
p2.load_json(p1.json())
print(p2)

persons3 = i6.List(p2)

print(persons3)
persons3.load_json(persons.json())
print(persons3)
