"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

from race import Race

class SatyrRace(Race):
    def __init__(self):
        super().__init__("Satyr", max_hp=25)

    def innate_tick(self, world, player):
        player.resources.setdefault("bound", 10)
        player.resources.setdefault("is_bounding", False)

        if not player.resources["is_bounding"] and player.resources["bound"] < 10:
            player.resources["bound"] += 1
        elif player.resources["is_bounding"]:
            player.resources["bound"] -= 1
            if player.resources["bound"] <= 0:
                player.resources["is_bounding"] = False
                player.spd = 1

    def ability_one(self, world, player):
        # Head Charge
        pass

    def ability_two(self, world, player):
        # Toggle Bound
        if not player.resources.get("is_bounding", False):
            player.resources["is_bounding"] = True
            player.spd = 2
        else:
            player.resources["is_bounding"] = False
            player.spd = 1