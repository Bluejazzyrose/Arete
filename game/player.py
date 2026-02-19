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