from unit import Player
from world import Room
from item import Item

def game_loop(player):
    while True:
        command = input("> ").strip().lower()
        
        if command in ["quit", "exit"]:
            print("Thank you for playing!")
            break

        elif command.startswith("go "):
            direction = command[3:]
            current_room = player.location
            if direction in current_room.exits:
                next_room = current_room.get_exit(direction)
                if next_room.is_locked():
                    print("The door is locked. You need a key to unlock it.")
                else:
                    player.move(next_room)
                    enter_room(next_room)

        elif command.startswith("look"):
            print(player.location)

        
            
                 


def enter_room(room):
    """
    Function to enter a room and display its description.
    """
    print(f"You enter the {room.name}.")
    print(room.description)
    print(f"You see:{room.interactables}")
    print(f"Exits: {', '.join(room.exits.keys())}")

def describe_room(room):
    return room.description

def list_items(items):
    if items:
        print("You see the following items:")
        for item in items:
            print(f"- {item.name}: {item.description}")
    else:
        print("There are no items here.")
    
    