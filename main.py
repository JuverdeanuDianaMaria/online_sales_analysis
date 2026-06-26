from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop", 3000, 2)
p2 = Product("Mouse", 100, 5)
p3 = Product("Keyboard", 200, 3)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.display_products()

print("Valoarea totala:", manager.total_value(), "lei")