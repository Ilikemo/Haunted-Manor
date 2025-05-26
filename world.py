from item import Item

class Room:
    def __init__(self, name, description, interactables, mob = None, locked=False, key=None, door_description = None):
        self.name = name
        self.description = description
        self.door_description = door_description or "You see a wooden door."
        self.exits = {}                     #exits is a dictionary of directions and corresponding rooms
        self.interactables = interactables  #interactables is a list of objects that can be interacted with in the room
        self.mob = mob                      
        self.locked = locked
        self.key = key

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)
    
    def is_locked(self):
        return self.locked
    
    def describe_door(self):
        return self.door_description
    
    def unlock(self, key):
        if self.locked and key == self.key:
            self.locked = False
            print(f"You unlock the door with the {key.name}.")
        elif self.locked:
            print("The door remains locked.")
        else:
            print("The door is already unlocked.")

    def print_interactables(self):
        if self.interactables:
            print("You see the following items:")
            for item in self.interactables:
                print(item)
        else:
            print("There are no items to interact with here.")

    def print_exits(self):
        if self.exits:
            print("Exits:")
            for direction, room in self.exits.items():
                print(f"- {direction}: {room.name}")
        else:
            print("There are no exits from this room.")

    def take_item(self, player, item):
        if isinstance(item, Item):
            if item in self.interactables:
                self.interactables.remove(item)
                print(f"You take the {item.name}.")
                player.add_item(item)
                return
        elif item in self.interactables:
            print(f"You can not take {item}.")
        else:
            print(f"There is no {item} here to take.")

            
class Container:
    def __init__(self, name, description, items=None, key=None, is_locked=False):
        self.name = name
        self.description = description
        self.items = items if items is not None else []
        self.key = key
        self.is_locked = is_locked

    def __str__(self):
        return f"{self.name}(container): {self.description} (Locked: {self.is_locked})" 
    
    def unlock(self, key):
        if self.is_locked and key == self.key:
            self.is_locked = False
            print(f"You unlock the {self.name} with the {key.name}.")
        elif self.is_locked:
            print("You don't have the key to unlock this container.")
        else:
            print("The container is already unlocked.")

    def interact(self, player):
        if self.is_locked:
            print(f"The {self.name} is locked. You need a key to open it.")
            response = input("Would you like to try to use a key if you have it? (yes/no) ")
            print("\n")
            if response.lower() == "yes":
                if self.key in player.inventory:
                    player.remove_item(self.key)
                    self.unlock(self.key)
            if response.lower() == "no":
                print("You decide not to use a key.")
                return
        if self.items:
            print(f"You open the {self.name} and find:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")
            response = input("Would you like to take the items? (yes/no) ")
            print("\n")
            if response.lower() == "yes":
                for item in self.items:
                    player.add_item(item)
                self.items.clear()
                print("You take the items.")
            else:
                print("You leave the items in the container.")
        else:
            print(f"The {self.name} is empty.")

            

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        