"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

from ..race import Race

class DryadRace(Race):
    def __init__(self):
        super().__init__("Dryad", max_hp=50)

    def innate_tick(self, world, player):
        if world.get_space_type(player.position) == "outdoor":
            player.resources.setdefault("photosynthesis", 0)
            player.resources["photosynthesis"] += 1

            if player.resources["photosynthesis"] >= 10:
                if player.hp < self.max_hp:
                    player.hp += 1
                player.resources["photosynthesis"] = 0

    def ability_one(self, world, player):
        # Grappling Vines
        pass

    def ability_two(self, world, player):
        # Healing Shrub
        world.spawn_entity(
            entity_type="DryadPlant",
            position=player.position
        )