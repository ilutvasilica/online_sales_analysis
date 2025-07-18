
from product import Product
from product_manager import ProductManager
from cart import Cart
import random 

manager = ProductManager()

p1 = Product("Laptop Gaming",5500,4)
p2 = Product("Telefon Smart",2400,8)
p3 = Product("Casti Wireless",300,12)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

print("\nProduse disponibile:")
manager.show_products()

total = manager.total_inventory_value()

print(f"\nValoarea totala a stocului: {total:.2f} $.")


cart = Cart()

products = manager.products

for _ in range(3):
    product = random.choice(products)
    max_quantity = min(product.quantity, 3)
    if max_quantity > 0:
        quantity = random.randint(1, max_quantity)
        cart.add_to_cart(product, quantity)

print("\nThe cart contains:")
cart.show_cart()

print(f"\nTotal amount: {cart.calculate_total():.2f} RON")




