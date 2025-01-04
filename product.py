from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    name: str
    description: str
    price: int
    id: Optional[int] = None