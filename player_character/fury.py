"""
Author: Jasmine Frye
Program: Mythos game (name is a placeholder)
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Fury race child class, derived from Player
"""

from player_character.player import Player

"""
Fury Character Class
Steals health from allies
Spends health to deal massive damage
"""
class Fury(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 10    #max hp is 10
        self.race = "Fury"
        self.friendly_fire = False
        self.kindled_on = False
        self.kindling = 0
    def __repr__(self):
        return f"{self.username} - race: Fury, max hp: 10 ({self.hp} remaining)."

    """
    X / E: Kindled Fury
        or Scream if 0 hp
    """
    def one_ability(self):
        if self.kindled_on:
            self.kindled_on = False
            self.hp -= self.kindling
            self.kindling = 0
        else:
            self.kindled_on = True

    """
    Y / Q: Friendly Fire
    """
    def two_ability(self):
        if self.friendly_fire:
            self.friendly_fire = False
        else:
            self.friendly_fire = True

    """
    innate_ability: track ghostly status and kindling
    if the fury runs out of hp, set status to ghostly
    if kindled fury is activated, progress kindling
    """
    def innate_ability(self, space_type):
        # check if status should be ghostly
        if self.hp < 1:
            self.status = 'ghostly'
            self.hp = 0
        elif self.hp > 9 and self.status == 'ghostly':
            self.status = 'none'
        # progress kindling if kindled fury is activated
        elif self.kindled_on:
            if self.kindling < 10:
                self.kindling += 1
            if self.kindling > 9:
                print('Maximum potency for Kindled Fury has been reached.')
                print('Release now to deal massive damage.')
            print(f'Current damage potential is {self.kindling * self.kindling}.')

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 10
        self.friendly_fire = False
        self.kindled_on = False
        self.kindling = 0