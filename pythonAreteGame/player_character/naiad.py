"""
Author: Jasmine Frye
Program: Mythos game (name is a placeholder)
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Naiad race child class, derived from Player
"""

from player_character.player import Player

"""
Naiad Character Class
Self-healing and crowd control abilities
Good at evading damage
"""
class Naiad(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 25    #max hp is 25
        self.race = "Naiad"
        self.aqua = 0
        self.puddle = False

    def __repr__(self):
        return f"{self.username} - race: Naiad, max hp: 25 ({self.hp} remaining)."

    """
    X / E: Create Puddle
    """
    def one_ability(self):
        return [[self.x, self.y],[self.x, self.y - 1],[self.x, self.y + 1],
                [self.x - 1, self.y],[self.x - 1, self.y - 1],[self.x - 1, self.y + 1],
                [self.x + 1, self.y],[self.x + 1, self.y - 1],[self.x + 1, self.y + 1],]

    """
    Y / Q: Become Puddle
    FUTURE: pause every other function, including healing and taking damage
    """
    def two_ability(self):
        if self.puddle:
            self.puddle = False
        elif not self.puddle:
            self.puddle = True
        print(f"Now in puddle form: {self.puddle}.")

    """
    innate_ability: Aquatic Regeneration
    every 5 aquatic spaces traversed increases current hp by 1, to max
    added logic in Mythos: if on aquatic space, increase aqua
    """
    def innate_ability(self, space_type):
        if space_type == 'aquatic' and not self.puddle:
            self.aqua += 1
        if self.aqua > 4 and self.hp < 25:
            self.hp += 1
            self.aqua = 0
            print("You've healed 1 hp via aquatic regeneration!")

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 25
        self.aqua = 0
        self.puddle = False