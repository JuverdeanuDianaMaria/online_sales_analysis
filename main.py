from product import Product
from product_manager import ProductManager


manager = ProductManager()

p1 = Product("Gaming Laptop", 3000, 1)
p2 = Product("Wireless Mouse", 100, 2)
p3 = Product("Mechanical Keyboard", 200, 1)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
