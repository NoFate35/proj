from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class User:
    first_name: str
    last_name: str
    address: str
    id: Optional[int] = None
    cars: List['Car'] = field(default_factory=list)

    def add_car(self, car: 'Car'):
        self.cars.append(car)
