"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player class
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

    @classmethod
    def load(cls, filepath):
        with open(filepath) as f:
            data = json.load(f)

        race = RaceFactory.create(data["race"])

        player = cls(
            username=data["username"],
            race=race,
            x=data["position"]["x"],
            y=data["position"]["y"]
        )

        player.hp = data["stats"]["hp"]
        player.status = data["stats"]["status"]
        player.inventory = data["inventory"]

        return player
    
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