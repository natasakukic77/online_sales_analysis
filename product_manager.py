from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_prod(self, product):
        self.products.append(product)
        
    def display_all_prod(self):
        print (f"Available products:")
        for product in self.products:
            product.display_info()
            
    def total_price(self):
        total = sum(product.price for product in self.products)
        return total
        
    def remove_product_by_name(self,product_name):
        self.products = [product for product in self.products if product != product_name]
      
    def list_products(self):
        return self.products
        

        
    