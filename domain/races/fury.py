"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

from Arete.domain.race import Race

class FuryRace(Race):
    def __init__(self):
        super().__init__("Fury", max_hp=10)

    def innate_tick(self, world, player):
        if player.hp <= 0:
            player.status = "ghostly"
            player.hp = 0

        player.resources.setdefault("kindled_on", False)
        player.resources.setdefault("kindling", 0)

        if player.resources["kindled_on"]:
            player.resources["kindling"] += 1

    def ability_one(self, world, player):
        # Toggle Kindled Fury
        if player.resources["kindled_on"]:
            damage = player.resources["kindling"] ** 2
            player.hp -= player.resources["kindling"]
            player.resources["kindling"] = 0
            player.resources["kindled_on"] = False
            # world.apply_damage(...)
        else:
            player.resources["kindled_on"] = True

    def ability_two(self, world, player):
        # Toggle Friendly Fire
        player.resources["friendly_fire"] = not player.resources.get("friendly_fire", False)