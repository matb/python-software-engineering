import dataclasses
import enum
import random
import typing


class ItemType(str, enum.Enum):
    weapon = "weapon"
    consumable = "consumable"
    utility = "utility"


class Item(typing.Protocol):
    name: str
    type: ItemType
    qty: int

    def use(self):
        ...

@dataclasses.dataclass
class Weapon:
    name: str
    qty: int
    dmg: int
    acc: float
    type: ItemType = ItemType.weapon

    def use(self):
        return self.attack()

    def attack(self):
        if random.random() <= self.acc:
            return self.dmg
        else:
            print("Hero misses")
            return 0

@dataclasses.dataclass
class Pan:
    name: str = "PAN"
    qty: int = 1
    type: ItemType = ItemType.utility

    def use(self):
        print("You cook a delicious meal")
        print("Though you now have to clean it")
        return 0