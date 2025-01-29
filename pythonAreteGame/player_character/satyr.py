"""
Author: Jasmine Frye
Program: Mythos game (name is a placeholder)
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Satyr race child class, derived from Player
"""

from player_character.dryad import DryadPlant
from player_character.player import Player

"""
Satyr Character Class
Abilities with high mobility and horns that damage attackers
Can regain hp by eating Dryad plants
"""
class Satyr(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 25  # max hp is 25
        self.race = "Satyr"
        self.bound = 10  # max bound is 10
        self.is_bounding = False

    def __repr__(self):
        return f"{self.username} - race: Satyr, max hp: 25 ({self.hp} remaining)."

    """
    interact method override: eat dryad plants
    In addition to interacting with normal objects,
    Satyrs can also interact with plants left by Dryads
    """
    def check_heal(self, interactee):
        healed = False
        if isinstance(interactee, DryadPlant):
            healed = True
            if interactee.is_tree:
                if self.hp < 15:
                    self.hp += 10
                elif self.hp < 25:
                    self.hp = 25
                else:
                    healed = False
            else:
                if self.hp < 20:
                    self.hp += 5
                elif self.hp < 25:
                    self.hp = 25
                else:
                    healed = False
        return healed

    """
    X / E: Head Charge
    charge in the direction faced until you hit a wall
    pinned enemies take 5 dmg
    """
    def one_ability(self):
        pass

    """
    Y / Q: Bound
    move 2x speed for up to 30 seconds
    toggles the ability on or off depending what the current status is
    and adjusts the speed accordingly
    """
    def two_ability(self):
        if not self.is_bounding:
            self.is_bounding = True
            self.spd = 2
        else:
            self.is_bounding = False
            self.spd = 1

    """
    innate_ability: Sharp Horns
    deal 2 dmg to any mobs in the same space
    # add logic in Mythos: check space for mobs after each action
    # no logic for this in Satyr??
    
    innate_ability logic progresses and monitors bound
    if two_ability is off, increase bound per space to max
    if two_ability is on, decrease bound per space to 0
    """
    def innate_ability(self, space_type):
        if not self.is_bounding and self.bound < 10:
            self.bound += 1
        elif self.bound > 0:
            self.bound -= 1
        else:
            self.two_ability()

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 25
        self.bound = 10
        self.is_bounding = False