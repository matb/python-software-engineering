import typing
import dataclasses

@dataclasses.dataclass
class Person:
    name: str


class Employee(Person):
    role: str
    manager: typing.Optional[Person] = None


NO_MANAGER = Person(name="no acting manager")

class Employee(Person):
    role: str
    manager: Person = None

employees = [Employee]

for e in employees:
    if e.manager:
        m = e.manager.name
    else:
        m = 'No acting manager'
    print(e.name, '-', m)