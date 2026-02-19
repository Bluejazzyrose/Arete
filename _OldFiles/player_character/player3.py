"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

class Player:
    def __init__(self, username, position, race):
        self.username = username
        self.position = position
        self.race = race

        self.hp = race.max_hp
        self.status = None
        self.spd = 1

        # general-purpose resource container
        self.resources = {}


class Race:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp

    def innate_tick(self, world, player):
        pass


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


class NaiadRace(Race):
    def __init__(self):
        super().__init__("Naiad", max_hp=25)

    def innate_tick(self, world, player):
        player.resources.setdefault("aqua", 0)
        player.resources.setdefault("puddle", False)

        if world.get_space_type(player.position) == "aquatic" and not player.resources["puddle"]:
            player.resources["aqua"] += 1

            if player.resources["aqua"] >= 5:
                if player.hp < self.max_hp:
                    player.hp += 1
                player.resources["aqua"] = 0

    def ability_one(self, world, player):
        # Create puddle AoE area
        pass

    def ability_two(self, world, player):
        player.resources["puddle"] = not player.resources.get("puddle", False)