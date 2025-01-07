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
