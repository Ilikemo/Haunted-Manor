from item import Item
from unit import Player
from world import Room


def enter_room(room):
    """
    Function to enter a room and display its description.
    """
    print(f"You enter the {room.name}.")
    print(room.description)
    print(f"You see:{room.interactables}")
    print(f"Exits: {', '.join(room.exits.keys())}")
    
    