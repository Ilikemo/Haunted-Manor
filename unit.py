class unit:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        if self.health <= 0:
            raise ValueError("Health must be greater than 0.")
        
    def attack(self, target):
        if target.health > 0:
            print(f"{self.name} attacks you for {self.damage} damage.")
            target.health -= self.damage
            if target.health <= 0:
                print(f"you have been defeated by {self.name}!")
        else:
            print(f"{self.name} is already defeated.")



class Player(unit):
    def __init__(self):
        super().__init__(name="Player", health=100, damage=10)
        self.location = None
        self.inventory = []
        
    def move(self, new_location):
        if new_location is not None:
            self.location = new_location
        else:
            print("You can't move to that location.")
    
    def use_item(self, item):
        if item in self.inventory:
            print(f"You use the {item}.")
            self.inventory.remove(item)
            item.use(self)
        else:
            print(f"You don't have a {item} in your inventory.")
        
    def add_item(self, item):
        if item is not None:
            self.inventory.append(item)
        else:
            print("You can't add a None item to your inventory.")
    
    def attack(self, target):
        if target.health > 0:
            print(f"You attack {target.name} for {self.damage} damage.")
            target.health -= self.damage
            if target.health <= 0:
                print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name} is already defeated.")