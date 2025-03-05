from product_manager import ProductManager
from product import Product
from cart import Cart

manager = ProductManager()
cart = Cart()

product1 = Product("Aquarelle colour pencils",250,20)
product2 = Product ("Canvas", 70, 200)
product3 = Product("Oil paint",133, 45)
product4 = Product ("Set of brushes", 120, 80)
product5 = Product ("Pastels", 300, 52)
product6 = Product ("Sketchbook", 25, 500)

manager.add_prod(product1)
manager.add_prod(product2)
manager.add_prod(product5)

manager.display_all_prod()

print(f"Total price of all products: {manager.total_price()}$")

manager.remove_product_by_name("Canvas")
print(manager.list_products())