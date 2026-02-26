"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Race factory to register race types into a usable list
"""

# race_factory.py
class RaceFactory:
    _races = {}

    @classmethod
    def register(cls, race_class):
        cls._races[race_class.name] = race_class

    @classmethod
    def create(cls, race_name):
        race_class = cls._races.get(race_name)

        if not race_class:
            raise ValueError(f"Unknown race: {race_name}")

        return race_class()
