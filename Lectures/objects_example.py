# Define a new type of data
class Product:

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


pina_bar = Product("Piña Chocolotta", 7.99,["200 calories", "24 g sugar"])

pina_bar.increase_inventory(1)
Product.increase_inventory(pina_bar,1)  # equivalent

print(pina_bar.get_inventory_report())
print(pina_bar.inventory) 

pina_bar.reduce_inventory(2)
print(pina_bar.get_inventory_report())
print(pina_bar.inventory) 

truffle_bar = Product("Trufflapagus", 9.99, ["170 calories", "19 g sugar"])
truffle_bar.increase_inventory(1)
bars = [pina_bar, truffle_bar]
print(f"truffle_bars = {bars[1].inventory}")
