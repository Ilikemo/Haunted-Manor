from unit import Player
from world import Room
from item import Item
import random

class GameOver(Exception):
    """Custom exception to handle game over scenarios."""
    pass

def game_loop(player):
    print("Welcome to the Manor!")
    print("Type 'quit' or 'exit' at any time to exit the game.")
    print("You find yourself in a dark room.")
    enter_room(player.location, player)
    # Main game loop
    while True:
        
        command = input("> ").strip().lower()
        
        if command in ["quit", "exit"]:
            print("Thank you for playing!")
            raise GameOver("Game exited by user.")

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

        
            
                 
def enter_room(room, player):
    """
    Function to enter a room and display its description.
    """
    print(f"You enter the {room.name}.")
    print(room.description)
    print(f"You see:{room.interactables}")
    print(f"Exits: {', '.join(room.exits.keys())}")
    if room.mob:
        print(f"You see the following creature:{room.mob.name}")
        combat(room.mob, player)

def combat(mob, player):
    while mob.is_alive() and player.is_alive():
        print(f"{player.name} (Health: {player.health}) vs {mob.name} (Health: {mob.health})")
        action = input("Do you want to (a)ttack, (u)se and item, or attempt to (r)un? ").strip().lower()
        if action == "a":
            player.attack(mob)
            if mob.is_alive():
                mob.attack(player)
            else:
                break
        
        elif action == "u":
            if player.inventory:
                player.list_inventory()
                item_to_use = input("Which item do you want to use? ").strip().lower()
                for item in player.inventory:
                    if item.name.lower() == item_to_use:
                        player.use_item(item)
                        mob.attack(player)
                        break
                    else:
                        print(f"You don't have a {item_to_use} in your inventory.")

        elif action == "r":
            escape_chance = random.randint(1, 5)
            if escape_chance == 1:
                player.move(player.previous_location)
                print("You successfully escaped!")
                break
            else:
                print("You failed to escape!")
                mob.attack(player)
        
        elif action in ["quit", "exit"]:
            print("Thank you for playing!")
            raise GameOver("Game exited by user.")
        
        else:
            print("Invalid action.")
        if not player.is_alive():
            print("You have been defeated. Game over.")
            raise GameOver("Player defeated in combat.")
        
            
        

def describe_room(room):
    return room.description

def list_items(items):
    if items:
        print("You see the following items:")
        for item in items:
            print(f"- {item.name}: {item.description}")
    else:
        print("There are no items here.")
    
    