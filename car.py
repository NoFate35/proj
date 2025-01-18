from dataclasses import dataclass
from typing import Optional


@dataclass
class Car:
    manufacturer: str
    model: str
    plate: str
    color: str
    id: Optional[int] = None
    owner: Optional['User'] = None
    
    def get_manufacturer(self):
        return self.manufacturer
        
    def get_model(self):
        return self.model
    
    def get_plate(self):
        return self.plate
    
    def get_color(self):
        return self.color
        
    def set_id(self, id):
        self.id = id
    
    def set_owner(self, owner):
        self.owner = owner
    
    
    
