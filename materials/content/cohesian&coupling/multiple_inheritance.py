class A:
    def foo(self):
        print("A")


class B:
    def foo(self):
        print("B")


class C(A, B):
    """Nothing in here """


c = C()
c.foo()


class Employee:
    def __init__(self, salary: str, name: str):
        self.salary = salary
        self.name = name

    def work(self, task):
        print(f"{self.name} works on {task}")


class Dev(Employee):

    def __init__(self, name: str, salary: int, programming_language: str):
        super().__init__(self, salary)
        self.name = name
        self.programming_language = programming_language

    def code(self):
        super().work("coding in {self.programming_language}")


class Manager(Employee):

    def __init__(self, name: str, salary: int):
        super().__init__(self, salary, name)

    def manage(self, team: str):
        print(f"{self.name} manages {team}")


class TechLead(Dev, Manager):
    """
    An employee that does both - manage a team and can code
    Like a UNICORN
    """


# Mixins

class Employee:
    def __init__(self, salary: str, name: str):
        self.salary = salary
        self.name = name

    def work(self, task):
        print(f"{self.name} works on {task}")


class Dev(Employee):

    def __init__(self, name: str, salary: int, programming_language: str):
        super().__init__(self, salary)
        self.name = name
        self.programming_language = programming_language

    def code(self):
        super().work("coding in {self.programming_language}")


class ManagerMixIn:

    def manage(self, team: str):
        print(f"{self.name} manages {team}")


class TechLead(Dev, ManagerMixIn):
    """
    An employee that does both - manage a team and can code
    Like a UNICORN
    """



