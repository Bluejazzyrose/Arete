"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player class
"""

import json
from domain.race_factory import RaceFactory

class Player:
    # initializes a NEW character
    def __init__(self, username, position, race):
        self.username = username    # string that will correspond to the user's json file name
        self.position = position    # list with 2 ints
        self.race = race            # Race object

        self.hp = race.max_hp
        self.status = None
        self.spd = 1

        # general-purpose resource container
        self.resources = {}

    # loads a PREEXISTING character from data from a json file
    @classmethod
    def load(cls, data):
        # create a Race object from the character data
        race = RaceFactory.create(data["race"])

        # create a position variable from the character data
        position = (data["position"]["x"], data["position"]["y"])

        # create a Player object from the loaded and processed data
        player = cls(
            username=data["username"],
            position=position,
            race=race
        )

        # update changeable variables to reflect file data
        player.hp = data["stats"]["hp"]
        player.status = data["stats"]["status"]
        player.inventory = data["inventory"]

        # return the finished Player object
        return player
    
    # updates the player's position
    def move(self, direction, game_map):
        new_x, new_y = self.race.calculate_movement(
            direction, self.x, self.y, self.spd
        )

        space = game_map.validate_space(new_x, new_y)

        if space == "valid":
            self.x, self.y = new_x, new_y
        else:
            print("You cannot move there.")

    def interact(self, game_map):
        entity = game_map.get_entity_at(self.x, self.y)
        if entity:
            self.race.on_interact(self, entity)
        else:
            print("Nothing to interact with.")

    def one_ability(self, game_map):
        self.race.one_ability(self, game_map)

    def two_ability(self, game_map):
        self.race.two_ability(self, game_map)

    def process_passives(self, game_map):
        self.race.innate_ability(self, game_map)