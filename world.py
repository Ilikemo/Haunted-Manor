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
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        