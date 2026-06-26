from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

p1 = Product("Gaming Laptop", 3000, 1)
p2 = Product("Wireless Mouse", 100, 2)
p3 = Product("Mechanical Keyboard", 200, 1)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)


manager.display_products()

print("Valoarea totala:", manager.total_value(), "lei")

cart = Cart()

cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

print("\nProduse in cos:")
cart.display_cart()

print("Total de plata:", cart.total_price(), "lei")

