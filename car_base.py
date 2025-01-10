from carDAO import CarDAO


# BEGIN (write your solution here)
class CarBase:
    def __init__(self, conn):
        self.conn = conn
    def get_info(self, plate):
        car = CarDAO(self.conn)
        result = car.car_data(plate)
        
# END
