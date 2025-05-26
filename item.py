from item_actions import item_use_actions

class Item:
    def __init__(self, name, description, item_type, **kwargs):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.location_description = kwargs.get("location_description", "")  #description of where the item is found
        self.heal_amount = kwargs.get("heal_amount") 

    def __str__(self):
        return f"{self.name}: {self.description} (Type: {self.item_type})"

    def describe_location(self):
        if self.location_description:
            return f"You see a {self.name} here: {self.location_description}"
        return f"You see a {self.name} here."
    
    def use(self, player, target=None):
        if player is None:
            raise ValueError("Player cannot be None.")
        action = item_use_actions.get(self.item_type)
        if action:
            action(self, player, target)
        else:
            print(f"The {self.name} cannot be used")

    def __str__(self):
        return f"{self.name}: {self.description}"
        