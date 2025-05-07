

class item:
    def __init__(self, name, description, item_type, **kwargs):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.door_id = kwargs.get("door_id")
        self.heal_amount = kwargs.get("heal_amount") 

    def use(self, player, target=None):
        if player is None:
            raise ValueError("Player cannot be None.")
        if self.item_type == "potion":
            print(f"You use the {self.name}.")
            player.health += self.heal_amount
            print(f"You heal for {self.heal_amount} health.")
            if player.health >= 100:
                player.health = 100
                print("You are at full health.")
        elif self.item_type == "key":
            if target and target.door_id == self.door_id:
                print(f"You use the {self.name} on the door.")
                target.open()
            else:
                print(f"The {self.name} does not fit this door.")
        else:
            print(f"The {self.name} cannot be used in this way.")

    def __str__(self):
        return f"{self.name}: {self.description}"
        