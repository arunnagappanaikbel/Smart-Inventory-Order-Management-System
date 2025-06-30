import csv
from models.product import Product

class InventoryManager:
    def __init__(self, config, logger):
        self.file_path = config['data_paths']['products']
        self.logger = logger
        self.products = []
        self.load_products()
    
    def load_products(self):
        try:
            with open(self.file_path, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    p = Product(**row)
                    self.products.append(p)            
        except FileNotFoundError:
            self.logger.warning('File not found: starting from fresh')
            
            
    def add_products(self):
        sku = input("Enter SKU:")
        name = input("Enter name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        new_product = Product(sku, name, category, price, quantity)
        self.products.append(new_product)
        self.save_products()
        self.logger.info(f'sku {sku} added.')
        
    def save_products(self):
        with open(self.file_path, 'w', newline='') as f:
            writter = csv.DictWriter(f, fieldnames=["sku","name","category","price","quantity"])
            writter.writeheader
            for p in self.products:
                writter.writerow(p.to_dict())
                
    def get_low_stock(self, threshold=5):
        return [p for p in self.products if p.quantity <= threshold]