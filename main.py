"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Main py file
"""

from domain.load_races import load_all_races
from domain.player import Player

def main():
    # register races before anything tries to import them
    load_all_races()

    # test logic
    data = {
        "username": "Jazzyrose",
        "race": "Satyr",
        "position": {
            "x": 4,
            "y": 4,
            "map": "Plutus' Fields"
        },
        "stats": {
            "hp": 25,
            "status": None
        },
        "inventory": [
            {"item_id": "curio", "qty": 1}
        ]
    }
    player = Player.load(data)
    print(f"\n{player.username} is a {player.race} and has {player.hp} hp.")

    print("\nNo problems here!")

if __name__ == "__main__":
    main()