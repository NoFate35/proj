from dataclasses import dataclass
from typing import Optional


class Product:
    name: str
    title: str
    price: int
    id: Optional[int] = None