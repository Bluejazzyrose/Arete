"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

class Race:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp

    def innate_tick(self, world, player):
        pass