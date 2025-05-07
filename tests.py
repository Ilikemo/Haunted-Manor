from engine import *
from item import *
from unit import * 
from world import *
import unittest

def test_item_creation():
    """
    Test the creation of an item.
    """
    potion = item("Health Potion", "Heals 20 health.", "potion", heal_amount=20)
    assert potion.name == "Health Potion"
    assert potion.description == "Heals 20 health."
    assert potion.item_type == "potion"
    assert potion.heal_amount == 20
    assert potion.door_id is None
    assert potion.__str__() == "Health Potion: Heals 20 health."
    assert potion.use(None) == None


if __name__ == "__main__":
    test_item_creation()
    print("All tests passed.")