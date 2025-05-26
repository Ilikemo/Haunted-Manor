from unit import Player
from world import Room, Container
from item import Item
import random

class GameOver(Exception):
    """Custom exception to handle game over scenarios."""
    pass

def game_loop(player):
    print("Welcome to the Manor!")
    print("Type 'quit' or 'exit' at any time to exit the game.")
    enter_room(player.location, player)
    # Main game loop
    while True:
        print(f"You are in the: {player.location.name}")
        print("What would you like to do?")
        print("You can type 'go [direction]' to move, 'look' to look around, 'use [item]' to use an item,")
        print("'take [item]' to take an item, or 'interact [item]' to interact with an item.")
        print("\n")

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
                    enter_room(next_room, player)

        elif command.startswith("look"):
            print(player.location)
            player.location.print_interactables()
            player.location.print_exits()

        elif command.startswith("use "):
            item_used = command[4:]
            if not player.inventory:
                print("You have no items in your inventory.")
                continue
            if not item_used:
                player.list_inventory()
                item_used = input("Please specify an item to use.")
            if item_used == "back":
                continue
            for item in player.inventory:
                if item.name.lower() == item_used:
                    if item.item_type == "key":
                        player.location.print_exits()
                        direction = input("Which direction do you want to unlock? ").strip().lower()
                        for exit_direction, exit_room in player.location.exits.items():
                            if exit_direction == direction:
                                player.use_item(item, exit_room)
                    else:
                        player.use_item(item)
                    break
            else:
                print(f"You don't have a {item_used} in your inventory.")
            

        elif command.startswith("take "):
            item_taken = command[5:]
            if not player.location.interactables:
                print("There are no items to take here.")
                continue
            if not item_taken:
                player.location.print_interactables()
                item_taken = input("Please specify an item to take.")
            if item_taken == "back":
                continue
            for item in player.location.interactables:
                if item.name.lower() == item_taken:
                    player.location.take_item(player, item)
                    break
            else:
                print(f"There is no {item_taken} here to take.")

        elif command.startswith("interact "):
                box = command[9:]
                for item in player.location.interactables:
                    if item.name.lower() == box:
                        if isinstance(item, Item):
                            print(item.describe_location())
                            player.use_item(item)
                        elif isinstance(item, Container):
                            item.interact(player)
                        else:
                            print(f"You can't interact with {item.name}.")
                        break

    

        
            
                 
def enter_room(room, player):
    """
    Function to enter a room and display its description.
    """
    print(f"You enter the {room.name}.")
    print(room.description)
    print(f"You see:{', '.join(str(item) for item in room.interactables)}")
    print(f"Exits: {', '.join(room.exits.keys())}")
    if room.mob and room.mob.is_alive():
        print(f"You see the following creature:{room.mob.name}")
        combat(room.mob, player)

def combat(mob, player):
    while mob.is_alive() and player.is_alive():
        print(f"{player.name} (Health: {player.health}) vs {mob.name} (Health: {mob.health})")
        action = input("Do you want to (attack), (use) an item, or attempt to (run)? ").strip().lower()
        print("\n")
        if action == "attack":
            player.attack(mob)
            if mob.is_alive():
                mob.attack(player)
            else:
                break
        
        elif action == "use":
            if player.inventory:
                player.list_inventory()
                item_to_use = input("Which item do you want to use? (type 'back' to return)").strip().lower()
                if item_to_use == "back":
                    continue
                for item in player.inventory:
                    if item.name.lower() == item_to_use:
                        player.use_item(item)
                        mob.attack(player)
                        break
                else:
                    print(f"You don't have a {item_to_use} in your inventory.")
            else:
                print("You have no items in your inventory to use.")

        elif action == "run":
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
        
            
        


def list_items(items):
    if items:
        print("You see the following items:")
        for item in items:
            print(f"- {item.name}: {item.description}")
    else:
        print("There are no items here.")
    
    