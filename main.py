
from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop",4500,5)
p2 = Product("Telefon",2200,10)
p3 = Product("Casti",250,15)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

print("\nProduse disponibile:")
manager.show_products()

total = manager.total_inventory_value()

print(f"\nValoarea totala a stocului: {total:.2f} $.")

print("\nȘtergem produsul 'Telefon':")
manager.remove_product_by_name("Telefon")

print("\nProdusele după ștergere:")
manager.show_products()
