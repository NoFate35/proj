from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    name: str
    description: str
    price: int
    id: Optional[int] = None
'''
    def __iter__(self):
        print('self.dict', self.__dict__)
        return self.__dict__'''