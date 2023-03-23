from typing import Protocol

class Animal(Protocol):
    def eat(self):
        pass


class Dog:
    def eat(self):
        print("The dog eats.")


def feed_the_animal(animal: Animal) -> None:
    animal.eat()


dog = Dog()
feed_the_animal(dog)