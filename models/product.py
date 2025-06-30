class Product():
    def __init__(self, sku, name, category, price, quantity):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)
        
    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity    
        }