from unit import player

class room:
    def __init__(self, name, description, interactables, door_id = "wood", locked=False, key=None):
        self.name = name
        self.description = description
        self.exits = {}                     #exits is a dictionary of directions and corresponding rooms
        self.interactables = interactables  #interactables is a list of items that can be interacted with in the room
        self.door_id = door_id              #door_id is the color of the door corrisponding to the key
        self.locked = locked
        self.key = key


    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

    def __str__(self):
        return f"{self.name}: {self.description}"
    
