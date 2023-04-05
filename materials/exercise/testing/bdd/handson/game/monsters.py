import typing
import dataclasses


class Monster(typing.Protocol):
    hp: int
    name: str
    dmg: int
    acc: float


@dataclasses.dataclass
class Wolf:
    hp: int = 10
    name: str = "Wolf"
    dmg: int = 3
    acc: float = 0.5