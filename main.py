from engine import game_loop, GameOver
from unit import Player

def main():
    name = input("Welcome, what would you like to be called? ")
    if not name.strip():
        name = "Adventurer"
    player = Player(name, health=100, damage=10)
    
    
    try:
        game_loop(player)
    except GameOver:
        print("Exiting game...")





if __name__ == "__main__":
    main()