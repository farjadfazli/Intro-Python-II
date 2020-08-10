# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.location = location
        self.health = 100
        self.inventory = []
    
    def pickup_item(self, item):
        self.inventory.append(item)
        self.location.item.remove(item)
    
    def drop_item(self, item):
        self.inventory.remove(item)
        self.location.item.append(item)
    
    def print_inventory(self):
        print("Current inventory:")
        for item in self.inventory:
            print(item.name)