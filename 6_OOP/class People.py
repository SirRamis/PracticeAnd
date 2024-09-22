class People:
    def __init__(self, fio):
        self.fio = fio

    def get_name(self):
        parts = self.fio.split(' ')
        return parts[1]

    def set_fio(self, fio):
        self.fio = fio

p = People('rtgtr TRTR tyt')
print(p.get_name())

class PeopleList:
    def __init__(self):
        self.people = []

    def add_person(self, fio):
        self.people.append(People(fio))
    def __iter__(self):
        return iter(person.get_name() for person in self.people)

people_list = PeopleList()


people_list.add_person('rtyrt YUY hghg')
people_list.add_person('wef YUYI lolo')


for name in people_list:
    print(name)