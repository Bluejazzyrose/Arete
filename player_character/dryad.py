"""
Author: Jasmine Frye
Program: Mythos game (name is a placeholder)
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Dryad race child class, derived from Player
"""

from player_character.player import Player

class DryadPlant:
    def __init__(self, x, y, is_tree):
        #position on map
        self.x = x
        self.y = y
        #tree or shrub
        self.is_tree = is_tree

"""
Dryad Character Class
Self-healing and crowd control abilities
Dryad plants can benefit Satyrs
"""
class Dryad(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 50  # max hp is 50
        self.race = "Dryad"
        self.photosynthesis = 0
        self.dryad_plants = []

    def __repr__(self):
        return f"{self.username} - race: Dryad, max hp: 50 ({self.hp} remaining)."

    """
    X / E: grappling vines
    3x3 AoE, 10 move cooldown
    ROOTS non-flying entities for 5 moves
    """
    def one_ability(self):
        pass

    """
    Y / Q: healing shrub
    heal 5 hp; places a DryadPlant shrub
    Satyrs can eat shrub for same effect
    Photosynthesis is set back to monitor frequency of use
    """
    def two_ability(self):
        if self.photosynthesis > -1:
            #place dryad shrub at current position
            self.dryad_plants.append(DryadPlant(self.x, self.y, False))

            #heal 5 hp
            if self.hp < 45:
                self.hp += 5
            elif self.hp < 50:
                self.hp = 50

            #set back photosynthesis to monitor frequency of use
            self.photosynthesis = -10

    """
    innate_ability: photosynthesis
    every 10 outdoor spaces traversed increases current hp by 1, to max
    if on outdoor space, increase photosynthesis
    """
    def innate_ability(self, space_type):
        if space_type == 'outdoor':
            self.photosynthesis += 1
        if self.photosynthesis > 9 and self.hp < 50:
            self.hp += 1
            self.photosynthesis = 0
            print("You've healed 1 hp via photosynthesis!")

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 50
        self.photosynthesis = 0
