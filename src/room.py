# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, *item):
        self.name = name
        self.description = description
        self.item = list(item)
    
    def __str__(self):
        if self.item:
            return (f"You are now at {self.name}. {self.description} \n There is a {','.join(item.name for item in self.item)} in the room. Type `get [item name]` to pick it up!")
        else:
            return f"You are now at {self.name}. {self.description} \n There is no item in the room."