# Define a new type of data
class Product:
    sales_tax = 0.07
    # Set the initial values
    def __init__(self, name, price, nutrition_info):
        self.name = name
        self.price = price
        self.nutrition_info = nutrition_info
        self.inventory = 0

    # Define methods
    def increase_inventory(self, amount):
        self.inventory += amount

    def reduce_inventory(self, amount):
        self.inventory -= amount

    def get_inventory_report(self):
        if self.inventory == 0:
            return "There are no bars!"
        return f"There are {self.inventory} bars."

    def get_total_price(self, quantity):
        return round((self.price * (1 + self.sales_tax)) * quantity,2)


pina_bar = Product("Piña Chocolotta", 7.99,
    ["200 calories", "24 g sugar"])
truffle_bar = Product("Trufflapagus", 9.99, 
    ["170 calories", "19 g sugar"])

Product.sales_tax = 0.10
pina_bar.sales_tax = .08
Product.sales_tax = 0.09
print(f"pina_bar sales tax = {pina_bar.sales_tax}")
print(f"truffle_bar sales tax = {truffle_bar.sales_tax}")
print(f"price of 4 pina_bars = {pina_bar.get_total_price(4):.2f}")
print(f"price of 4 truffle_bars = {truffle_bar.get_total_price(4):.2f}")

