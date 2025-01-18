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
    
    def get_owner(self):
        return self.first_name + ' ' + self.last_name
    
    def get_address(self):
        return self.address
    
    def set_id(self, id):
        self.id = id