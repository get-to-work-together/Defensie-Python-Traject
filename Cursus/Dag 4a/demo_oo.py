
class Person:

    __slots__ = ['_name', '_residence']

    # magic methods
    def __init__(self, n, r):
        # attributen
        self._name = n
        self._residence = r

    def __repr__(self):
        return f'Person("{self._name}", "{self._residence}")'

    def __str__(self):
        return f'{self._name} uit {self._residence}'

    # methods
    def tell(self):
        print(f'Ik ben {self._name} en ik woon in {self._residence}.')

    def move(self, new_residence):
        self._residence = new_residence
        print(f'Ik ben verhuisd naar {new_residence}.')


from dataclasses import dataclass

@dataclass
class Person:
    # attributen
    _name: str
    _residence: str

    # magic methods
    def __str__(self):
        return f'{self._name} uit {self._residence}'

    # methods
    def tell(self):
        print(f'Ik ben {self._name} en ik woon in {self._residence}.')

    def move(self, new_residence):
        self._residence = new_residence
        print(f'Ik ben verhuisd naar {new_residence}.')


class Customer(Person):

    def tell(self):
        print(f'Ik ben een klant en ik heet {self._name} en ik woon in {self._residence}.')

# ------------------------------------

p1 = Person('Peter', 'Lhee')  # instantiëren en initieer
p2 = Customer('Stefan', 'Hoogeveen')  # instantiëren en initieer

p1.tell()

p2.tell()
# ===> omgezet naar
Person.tell(p2)

p1.move('Amsterdam')
p1.tell()

print(repr(p1))
print(str(p1))

p1.tell()
