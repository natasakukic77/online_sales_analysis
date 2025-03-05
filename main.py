from product_manager import ProductManager
from product import Product

manager = ProductManager()

product1 = Product("woodworking tools",250,40)
product2 = Product ("hammer", 70, 100)
product3 = Product("chisels",133, 13)

manager.add_prod(product1)
manager.add_prod(product2)
manager.add_prod(product3)


manager.remove_product_by_name("Canvas")
print(manager.list_products())