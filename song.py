from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:
    title: str
    artist_name: str
    id: Optional[int] = None