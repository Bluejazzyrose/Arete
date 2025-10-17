"""
Author: Jasmine Frye
Program: Mythos game (name is a placeholder)
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent class
"""

class Player:
    def __init__(self, name):
        self.username = name
        self.x = 8
        self.y = 8
        self.spd = 1
        self.status = 'none'
        # inventory currently does nothing, but is prepped and ready for future iterations
        # self.inventory = pandas.read_csv('inventory.csv')

    def one_ability(self):
        pass
    def two_ability(self):
        pass
    def innate_ability(self, space_type):
        pass
    def rest(self):
        print('All stats and abilities have been reset to original values and status.')
        self.status = 'none'