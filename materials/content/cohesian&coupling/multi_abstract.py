from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def eat(self):
        pass
    
    
class Reptile(Animal, ABC):
    
    @abstractmethod
    def lay_egg(self):
        pass
    
class Mamal(Animal, ABC):
    
    @abstractmethod
    def breath_air(self):
        pass