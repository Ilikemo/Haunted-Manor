import random

class Unit:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        if self.health <= 0:
            raise ValueError("Health must be greater than 0.")
        
    def attack(self, target):
        attack_damage = (self.damage + random.randint(-10, 5))
        if target.health > 0:
            print(f"{self.name} attacks you for {attack_damage} damage.")
            target.health -= attack_damage
            target.grave_wound()
        else:
            print(f"{self.name} is already defeated.")
    
    def is_alive(self):
        return self.health > 0



class Player(Unit):
    def __init__(self):
        super().__init__(name="Player", health=100, damage=10)
        self.location = None
        self.previous_location = None
        self.inventory = []
        
    def move(self, new_location):
        if new_location is not None:
            self.previous_location = self.location
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

    def grave_wound(self):
        if self.health <= 0:
            print("You have lost your head")
        elif self.health <= 20:
            print("You are gravely wounded and lose your arm.")
        elif self.health <= 50:
            print("You are wounded and lose a fingernail.")