from car import Car
from user import User

from psycopg2.extras import NamedTupleCursor


class CarDAO:
    def __init__(self, conn):
        self.conn = conn

# BEGIN (write your solution here)
    def car_data(self, plate):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            sql = "SELECT cars.manufacturer, cars.model, cars.plate, cars.color, users.first_name, users.last_name, users.address FROM cars INNER JOIN users ON cars.user_id = users.id WHERE cars.plate = %s;"
            cur.execute(sql, (plate,))
            result = cur.fetchone()
            print('result', result)
# END
