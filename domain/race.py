"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

from domain.race_factory import RaceFactory

class Race:
    name = None
    max_hp = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.name is None:
            raise ValueError(f"{cls.__name__} must define a 'name' attribute.")
        
        if cls.max_hp is None:
            raise TypeError(f"{cls.__name__} must define 'max_hp'")

        RaceFactory.register(cls)

    def innate_tick(self, world, player):
        pass

    def ability1(self, world, player):
        pass

    def ability2(self, world, player):
        pass