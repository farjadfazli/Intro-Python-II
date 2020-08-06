# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
    
    def __str__(self):
        return f"You are now at {self.name}. {self.description} \n There is a {self.item.name} in the room."