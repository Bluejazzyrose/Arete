"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

from domain.race_factory import RaceFactory

class Race:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.name is None:
            raise ValueError(f"{cls.__name__} must define a 'name' attribute.")

        RaceFactory.register(cls)

    def innate_tick(self, world, player):
        pass

    def ability1(self, world, player):
        pass

    def ability2(self, world, player):
        pass