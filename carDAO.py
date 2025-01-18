from car import Car
from user import User

from psycopg2.extras import NamedTupleCursor


class CarDAO:
    def __init__(self, conn):
        self.conn = conn

# BEGIN (write your solution here)
    def car_data(self, plate):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            car_sql = "SELECT * FROM cars WHERE plate = %s;"
            cur.execute(car_sql, (plate,))
            car_result = cur.fetchone()
            #print('result', result.manufacturer)
            if car_result is None:
                return None
            car = Car(
                manufacturer = car_result.manufacturer,
                model = car_result.model,
                plate = car_result.plate,
                color = car_result.color,
                id = car_result.id
                )
                
            owner_id = car_result.user_id
            user_sql = "SELECT * FROM users WHERE id = %s;"
            cur.execute(user_sql, (owner_id,))
            user_result = cur.fetchone()
            user = User(
                first_name = user_result.first_name,
                last_name = user_result.last_name,
                address = user_result.address,
                id = user_result.id
                )
            car.owner = user
            return car
            
# END
