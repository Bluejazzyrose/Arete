"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

from ..race import Race

class NaiadRace(Race):
    def __init__(self):
        super().__init__(name="Naiad", max_hp=25)

    def innate_tick(self, world, player):
        player.resources.setdefault("aqua", 0)
        player.resources.setdefault("puddle", False)

        if world.get_space_type(player.position) == "aquatic" and not player.resources["puddle"]:
            player.resources["aqua"] += 1

            if player.resources["aqua"] >= 5:
                if player.hp < self.max_hp:
                    player.hp += 1
                player.resources["aqua"] = 0

    def ability1(self, world, player):
        # Create puddle AoE area
        pass

    def ability2(self, world, player):
        player.resources["puddle"] = not player.resources.get("puddle", False)