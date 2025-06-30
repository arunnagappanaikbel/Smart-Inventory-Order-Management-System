from modules.inventory import InventoryManager
from modules.orders import OrderManager
from modules.users import UserManager
from modules.reports import ReportGenerator
from utils.logger import setup_logger
import json


#Load config
with open('config/config.json') as f:
    config = json.load(f)
    
#Setup logger
logger = setup_logger(config['log_file'])

def main():
    logger.info("smart inventory management started")
    users = UserManager(config,logger)    
    inventory = InventoryManager(config, logger)
    reports = ReportGenerator(config, logger, inventory)
    orders = OrderManager(config, logger, inventory)
    
    
    try: 
        reports.generate_low_stock_report()
        users.add_user()
        inventory.add_products()
        orders.place_order()
    except Exception as e:
        logger.exception(f'unexpected error: {e}')
    
    

if __name__ == '__main__':
    main()
    
# ✅ Core Features & Modules
# 📦 1. Inventory Management
# Add/update/delete/search products.

# Product info: name, category, price, quantity, SKU, expiry (optional).

# Data stored in CSV and JSON.

# 🧾 2. Order Management
# Place new orders (multiple items).

# Automatically update stock levels.

# Store orders in text or binary files.

# Calculate totals, tax, discounts, etc.

# 👥 3. User Management (OOP)
# Users: Admins and Staff.

# Role-based access (Admins can do all operations; Staff can only process orders).

# Store users and roles securely (e.g., JSON file).

# 📂 4. Reports Module
# Low stock report.

# Top selling items.

# Daily/weekly order logs.

# Export to CSV.

# ⚙️ 5. Config Module
# Store settings like tax rates, discount %, data file paths, etc. in a config file (config.json).

