from product_manager import ProductManager
from product import Product

manager = ProductManager()

product1 = Product("Aquarelle colour pencils",250,20)
product2 = Product ("Canvas", 70, 200)
product3 = Product("Oil pastels",133, 45)

manager.add_prod(product1)
manager.add_prod(product2)
manager.add_prod(product3)

manager.display_all_prod()

print(f"Total price of all products: {manager.total_price()}$")