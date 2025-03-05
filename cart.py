from product import Product
#from product_manager import ProductManager


class Cart():
    def __init__(self):
        self.cart_items = []
        
    def add_cart_items(self,product):
        self.cart_items.append(product)
    
    def total_cart_price(self):
        return sum(product.price for product in self.cart_items)
    
    def display_cart_items(self):
        for product in self.cart_items:
            print (f"Product: {product.name}, price:{product.price}$")
        print(F"Total cost: {self.total_cart_price()}$")