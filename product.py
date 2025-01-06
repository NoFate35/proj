
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.id = None
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    