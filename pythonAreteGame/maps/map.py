"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Map class
"""
import pandas

from npc_mob_inanimate import Npc, Inanimate, Mob

"""
Map class
pulls data from a specified cvs file
keeps track of objects specific to the current map
"""
class Map:
    def __init__(self, mname):
        # dataframe to store spaces data
        mname = f'maps/{mname}.csv'
        self.spaces = pandas.read_csv(mname)

        # list to store entities data
        self.entities = []
        for index, row in self.spaces.iterrows():
            if row['object type'] == 'npc':
                self.entities.append(Npc(row['x'], row['y'], row['object name']))
            elif row['object type'] == 'inanimate':
                self.entities.append(Inanimate(row['x'], row['y'], row['object name']))
            elif row['object type'] == 'mob':
                self.entities.append(Mob(row['x'], row['y'], row['object name'],row['object status']))

    """
    get_space_type method
    verifies the type of space that the player is attempting to move to
    returns the space type
    """
    def get_space_type(self, x, y):
        # get the space type for the space being moved to/through
        for index, row in self.spaces.iterrows():
            if row['x'] == x and row['y'] == y:
                ns = row['space type']
                break
            else:
                ns = 'none'
        return ns

    """
    check_spaces method
    calls get_space_type method to verify space type
    returns the space type
    """
    def check_spaces(self, action, player):
        x = player.x
        y = player.y
        num = 0
        while num < player.spd:
            num += 1
            if action == 'w':
                y = player.y - num
            elif action == 'a':
                x = player.x - num
            elif action == 's':
                y = player.y + num
            elif action == 'd':
                x = player.x + num
            # get the space type for the space being moved to/through
            ns = self.get_space_type(x, y)
            # break from logic if there is an obstacle in the way
            if ns == 'impass':
                break
        return ns

    """
    change_map method
    changes the map and repositions the player accordingly
    reassigns entities accordingly with new map
    """
    def change_map(self, player):
        last_map = 'unknown'
        # remember the last map for player placement
        for index, row in self.spaces.iterrows():
            if row['x'] == 0 and row['y'] == 0:
                last_map = row['to']
        # change map
        for index, row in self.spaces.iterrows():
            if row['x'] == player.x and row['y'] == player.y:
                mname = f'maps/{row['to']}.csv'
        self.spaces = pandas.read_csv(mname)
        # reassign entities accordingly
        self.entities = []
        for index, row in self.spaces.iterrows():
            if row['object type'] == 'npc':
                self.entities.append(Npc(row['x'], row['y'], row['object name']))
            elif row['object type'] == 'inanimate':
                self.entities.append(Inanimate(row['x'], row['y'], row['object name']))
            elif row['object type'] == 'mob':
                self.entities.append(Mob(row['x'], row['y'], row['object name'], row['object status']))
        # reposition player appropriately
        for index, row in self.spaces.iterrows():
            if row['to'] == last_map:
                player.x = row['x']
                player.y = row['y']
        for e in self.entities:
            print(e)
        return player