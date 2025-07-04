
from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []
    def add_to_cart(self,product,quantity):
        
        if product.quantity >= quantity:
            new_product = Product(product.name,product.price,quantity)
            self.cart_items.append(new_product)
            print(f" '{product.name}' has been added to the cart {quantity} .  ")
        else:
            print(f"The stock is insufficient for the '{product.name}'")
            
    def calculate_total(self):
         return sum(product.price * product.quantity for product in self.cart_items)       
            
    def show_cart(self):
        if not self.cart_items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for item in self.cart_items:
                print(f"- {item.display_info()}")
                      