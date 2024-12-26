import psycopg2
from dataclasses import dataclass
from psycopg2.extras import execute_batch, execute_values, NamedTupleCursor, RealDictCursor, LoggingCursor, DictCursor

class Product:
    name: str
    title: str
    price: numeric
    id: Optional[int] = None