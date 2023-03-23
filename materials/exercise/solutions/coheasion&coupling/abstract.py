import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def eat(self):
        return super().eat()


dog = Dog()

def feed_the_animal(animal: Animal):
    animal.eat()
