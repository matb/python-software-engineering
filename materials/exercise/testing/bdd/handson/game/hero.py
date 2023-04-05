import dataclasses
import typing

from game.items import Item, ItemType
from game.monsters import Monster


@dataclasses.dataclass
class Hero:
    items: typing.List[Item]
    hp: int = 100

    def pick_up_item(self, item: Item):
        if len(self.items) >= 5:
            print(f"Pocket is full - cannot carry  {item}")
        else:
            self.items.append(item)

    def attack(self, use: str, target: Monster):
        weapon = None
        for i in self.items:
            if i.name == use:
                weapon = i
                break
        if not weapon or weapon.type != ItemType.weapon:
            raise ValueError(f"{use} is no available weapon")
        dmg = weapon.use()
        print(f"Hero does {dmg} damage")
        target.hp -= dmg