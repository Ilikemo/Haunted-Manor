from item_actions import item_use_actions

class Item:
    def __init__(self, name, description, item_type, **kwargs):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.door_id = kwargs.get("door_id")
        self.heal_amount = kwargs.get("heal_amount")

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
        