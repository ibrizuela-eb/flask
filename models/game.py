from dataclasses import dataclass


@dataclass
class Game:
    id: int
    name: str
    description: str
    price: float
