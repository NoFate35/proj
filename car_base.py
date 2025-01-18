from carDAO import CarDAO


# BEGIN (write your solution here)
class CarBase:
    def __init__(self, conn):
        self.conn = conn
    def get_info(self, plate):
        dao = CarDAO(self.conn)
        car = dao.car_data(plate)
        if car is None:
            raise KeyError ('Car is not found')

        return {
        "manufacturer": car.manufacturer,
        "model": car.model,
        "plate": car.plate,
        "color": car.color,
        "owner": car.owner.get_owner(),
        "owner_address": car.owner.address
        }
        
# END
