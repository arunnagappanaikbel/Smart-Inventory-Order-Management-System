import csv
class ReportGenerator:
    def __init__(self, config, logger, inventory):
        self.inventory = inventory
        self.logger = logger
        self.report_path = 'data/low_stock_report.csv'

    def generate_low_stock_report(self):
        low_stock_items = self.inventory.get_low_stock()
        with open(self.report_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["SKU", "Name", "Quantity"])
            for item in low_stock_items:
                writer.writerow([item.sku, item.name, item.quantity])
        self.logger.info("Low stock report generated.")