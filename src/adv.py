from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", Item("Sword", "A sharp sword!"), Item("Key", "A golden key")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("Wand", "A magic wand!"), Item("Ring", "A shiny ring!")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("Rock", "A hard rock!"), Item("String", "A piece of string!")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("Pen", "A blue pen!"), Item("Hat", "A top hat!")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item("Bulb", "A lightbulb!"), Item("Coin", "A silver coin!")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
while True:
#
# * Prints the current room name
    print(player.location)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    command = input("> ").split(' ')

    if command[0] == 'q':
        break

    elif command[0] == 'n':
        if hasattr(player.location, "n_to"):
            player.location = player.location.n_to
            
        else:
            print("\nYou can't go there!\n")

    elif command[0] == 's':
        if hasattr(player.location, "s_to"):
            player.location = player.location.s_to

        else:
            print("\nYou can't go there!\n")

    elif command[0] == 'e':
        if hasattr(player.location, "e_to"):
            player.location = player.location.e_to

        else:
            print("\nYou can't go there!\n")

    elif command[0] == 'w':
        if hasattr(player.location, "w_to"):
            player.location = player.location.w_to
    
        else:
            print("\nYou can't go there!\n")

    elif command[0].lower() == 'get':
        for item in player.location.item:
            if item.name.lower() == command[1].lower():
                player.pickup_item(item)
                player.print_inventory()
                break
    
    elif command[0].lower() == 'drop':
        for item in player.inventory:
            if item.name.lower() == command[1].lower():
                player.drop_item(item)
                player.print_inventory()
                break

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
