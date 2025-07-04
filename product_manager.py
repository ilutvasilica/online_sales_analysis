from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)    
        
    def show_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())    
                
    def total_inventory_value(self):
        total_value= sum(product.price *product.quantity for product in self.products)
        return total_value
    
    def remove_product_by_name(self, name):
        for product in self.products:
         if product.name.lower() == name.lower():
            self.products.remove(product)
            print(f"The product '{name}' has benn deleted.")
            return
        print(f"The product '{name}' was not found.")
                