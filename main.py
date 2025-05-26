from engine import game_loop, GameOver
from unit import Player
from world_loader import load_world

def main():
    name = input("Welcome, what would you like to be called? ")
    print("\n")
    if not name.strip():
        name = "Adventurer"
    player = Player(name)

    # Load the world
    rooms = load_world()
    player.location = rooms["foyer"]  # Set starting room

    try:
        game_loop(player)
    except GameOver:
        print("Exiting game...")

main()