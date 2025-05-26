import unittest
from unittest.mock import patch
from io import StringIO

from unit import Player, Unit
from item import Item
from world import Room, Container
from item_actions import use_potion, use_key
from engine import describe_room, list_items

class TestGame(unittest.TestCase):

    def test_player_initialization(self):
        player = Player()
        self.assertEqual(player.name, "Player")
        self.assertEqual(player.health, 100)
        self.assertEqual(player.damage, 10)
        self.assertEqual(player.inventory, [])

    def test_add_item_to_player_inventory(self):
        player = Player()
        potion = Item("Potion", "Restores HP", "potion", heal_amount=25)
        player.add_item(potion)
        self.assertIn(potion, player.inventory)

    def test_use_potion(self):
        player = Player()
        player.health = 50
        potion = Item("Potion", "Restores HP", "potion", heal_amount=30)
        player.add_item(potion)
        with patch('sys.stdout', new=StringIO()) as out:
            player.use_item(potion)
            self.assertIn("You use the Potion.", out.getvalue())
            self.assertEqual(player.health, 80)

    def test_use_key_unlocks_room(self):
        key = Item("Rusty Key", "Opens a door", "key", door_id="A1")
        room = Room("Hall", "A dark hallway", [], locked=True, key=key)
        with patch('sys.stdout', new=StringIO()) as out:
            use_key(key, None, room)
            self.assertFalse(room.locked)
            self.assertIn("You use the Rusty Key on the door.", out.getvalue())

    def test_room_take_item(self):
        player = Player()
        potion = Item("Potion", "Restores HP", "potion", heal_amount=20)
        room = Room("Room", "Test room", [potion])
        room.take_item(player, potion)
        self.assertIn(potion, player.inventory)
        self.assertNotIn(potion, room.interactables)

    def test_wrong_key_does_not_unlock(self):
        right_key = Item("Right Key", "Correct key", "key", door_id="A1")
        wrong_key = Item("Wrong Key", "Wrong key", "key", door_id="B2")
        room = Room("Room", "Locked", [], locked=True, key=right_key)
        with patch('sys.stdout', new=StringIO()) as out:
            room.unlock(wrong_key)
            self.assertTrue(room.locked)
            self.assertIn("The door remains locked.", out.getvalue())

    def test_container_add_remove(self):
        potion = Item("Potion", "Restores HP", "potion", heal_amount=20)
        chest = Container("Chest", "Dusty box")
        chest.add_item(potion)
        self.assertIn(potion, chest.items)
        chest.remove_item(potion)
        self.assertNotIn(potion, chest.items)

    def test_describe_room(self):
        room = Room("Room", "This is a room.", [])
        self.assertEqual(describe_room(room), "This is a room.")

    def test_list_items_output(self):
        potion = Item("Potion", "Restores HP", "potion", heal_amount=20)
        with patch('sys.stdout', new=StringIO()) as out:
            list_items([potion])
            self.assertIn("Potion: Restores HP", out.getvalue())

if __name__ == "__main__":
    unittest.main()
