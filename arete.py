"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""

import pandas
import os

from maps.map import Map
from player_character.satyr import Satyr


"""
Arete class
methods creating a framework for the game to run
METHOD LIST:
character creation methods: create_username, create_character
character loading methods:  build_character, load_character, save_character
gameplay methods/function:  move, interact, arete, main
"""

class Arete:
    def __init__(self, mname):
        # create Map from dataframe
        self.current_map = Map(mname)

    """
    move method
    changes the player's position
    checks for space inconsistencies using get_space
    """
    def move(self, action, player, current_map):
        new_space = current_map.check_spaces(action, player)
        # indicate if the edge of the map has been reached
        if new_space == 'none':
            print("You've reached the edge of the map and cannot move further in this direction.")
            print("To enter a new map use one of the portals.")
            print("If you just used a portal, exit the portal and reenter to traverse again.")
        # indicate obstacle
        elif new_space == 'impass':
            print("There is an obstacle blocking your way.")
        # change player coordinates
        else:
            if action == 'w':
                player.y = player.y - player.spd
            elif action == 'a':
                player.x = player.x - player.spd
            elif action == 's':
                player.y = player.y + player.spd
            elif action == 'd':
                player.x = player.x + player.spd
            # change maps
            if new_space == 'portal':
                player = current_map.change_map(player)
            # display new location
        print(f"Current position: {current_map.spaces.iloc[0]['space type']} - {player.x},{player.y}")
        return current_map

    """
    interact method
    checks the player's space for nonplayer entities
    engages with entities if they are present
    """
    def check_interact(self, player, cmap):
        interaction = False
        for o in cmap.entities:
            if o.x == player.x and o.y == player.y:
                o.interact()
                interaction = True
                # remove plants eaten by the satyr from the map - NOT FINISHED
                # maybe move this logic to the DryadPlant entity logic?
                if isinstance(player, Satyr):
                    ate = player.check_heal(o)
                    if ate:
                        pass
        # if there was nothing to interact with, say so
        if not interaction:
            print("There is nothing on this space to interact with.")

    """
    run_game method
    framework for the actively running game
    """
    def run_game(self, player, mname):
        # display current map name and entities with their respective positions
        print(f'\nLoading map... {self.current_map.spaces.iloc[0]['space type']}\n')
        for e in self.current_map.entities:
            print(e)

        # player action cycle - player action, mob actions, passive abilities
        while True:
            # player chooses an action
            action = (input("\nChoose an action (or 'x' to exit to menu): "))
            # move action
            if action.lower() == 'w' or action.lower() == 'a' or action.lower() == 's' or action.lower() == 'd':
                self.current_map = self.move(action, player, self.current_map)
            # attack action
            elif action.lower() == 'i' or action.lower() == 'j' or action.lower() == 'k' or action.lower() == 'l':
                pass
            # interact action
            elif action.lower() == 'n':
                self.check_interact(player, self.current_map)
            # view player stats
            elif action.lower() == 'p':
                print(player)
                continue
            # racial ability 1
            elif action.lower() == 'e':
                player.one_ability()
            # racial ability 2
            elif action.lower() == 'q':
                player.two_ability()
            # exit action
            elif action.lower() == 'x':
                return player, self.current_map
            # buttons that don't do anything
            else:
                print("Command had no effect.")
                continue

            # mobs would act here

            # use innate ability if appropriate
            player.innate_ability(self.current_map.get_space_type(player.x, player.y))
            # rejuvenate if at Elder Growth 8,8
            if player.x == 8 and player.y == 8 and self.current_map.spaces.iloc[0]['space type'] == 'Elder Growth':
                player.rest()
            # display status if there is one
            if player.status:
                print(f'Your current status is {player.status}')