def use_potion(item, player, target=None):
    if item.item_type == "potion":
            print(f"You use the {item.name}.")
            player.health = min(player.health + item.heal_amount, 100)
            print(f"You heal for {item.heal_amount} health.")
            if player.health == 100:
                print("You are at full health.")


def use_key(item, player, target):
    if item.item_type == "key":
        if target and target.key is item:
                print(f"You use the {item.name} on the door.")
                target.unlock(item)
                
        else:
            print(f"The {item.name} does not fit this door.")
    

item_use_actions = {
    "potion": use_potion,
    "key": use_key
}