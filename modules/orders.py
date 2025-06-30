from datetime import datetime
import pickle

class OrderManager:
    def __init__(self, config, logger, inventory):
        self.file_path = config['data_paths']['orders']
        self.logger = logger
        self.inventory = inventory
        
    def place_order(self):
        sku = input("Enter product SKU: ")
        quantity = int(input("Enter quantity to order: "))
        
        for product in self.inventory.products:
            if product.sku == sku:
                if product.quantity>=quantity:
                    product.quantity -=quantity
                    self.inventory.save_products()
                    order = {
                        'sku': sku,
                        'quantity': quantity,
                        'timestamp': datetime.now().isoformat()
                    }
                    self.save_order(order)
                    self.logger.info(f'Order is placed for sku {sku}')
                    return
                else:
                    print("insufficient stock")
        print("Product not found.")
        
        
    def save_order(self,order):
        try:
            with open(self.file_path, 'ab') as f:
                pickle.dump(order, f)
        except Exception as e:
            self.logger.error(f"Failed to save order: {e}")
        