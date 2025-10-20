"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""

import pandas

from maps.map import Map
from player_character.dryad import Dryad
from player_character.fury import Fury
from player_character.naiad import Naiad
from player_character.satyr import Satyr

import os

#xfile_path = 'C:\Users\jafrye02\OneDrive - Wayne State College\CSC310 Data Structures\GitHub Repositories\Arete\characters.csv'

# Get the absolute path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file (assuming it's in the same directory)
csv_file_name = "characters.csv"
absolute_csv_path = os.path.join(script_dir, csv_file_name)

# Read the CSV file using its absolute path
try:
    df = pandas.read_csv(absolute_csv_path)
    print("CSV file loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print(f"Error: The file '{absolute_csv_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

"""
Arete class
methods creating a framework for the game to run
METHOD LIST:
character creation methods: create_username, create_character
character loading methods:  build_character, load_character, save_character
gameplay methods/function:  move, interact, arete, main
"""

class Arete:
    def __init__(self):
        pass

    """
    create_username method
    prompts the user for input and returns a confirmed name choice
    """
    def create_username(self, characters):
        while True:
            name = input("What do you want to name your character? ")
            existent = False
            # verify no duplicate names in save file
            for index, row in characters.iterrows():
                if row['name'] == name:
                    print('There is already a character with that name.')
                    print('Please choose a different name.')
                    existent = True
                    break
            # if no duplicates, create character and save to file
            if not existent:
                while True:
                    y_n = input(f"Confirm: do you want to name your character {name}? y/n: ")
                    y_n = y_n.lower()
                    if y_n == 'y' or y_n == 'n':
                        break
                    else:
                        print("Invalid input. Please type 'y' or 'n'.")
                        continue
                if y_n == 'y':
                    break
            else:
                continue
        return name

    """
    create_character method
    menu for creating a new character
    calls create_username
    """
    def create_character(self):
        print("\nLet's create you a character!")
        print("Available Races")
        print("1. Dryad - 50 hp, good healing and crowd control. Best as tank or melee.")
        print("2. Satyr - 25 hp, high mobility, horns damage attackers. Best as melee.")
        print("3. Fury  - 10 hp, gains hp and spends it for massive dmg. Best as ranged.")
        print("4. Naiad - 25 hp, evades dmg, healing and crowd control. Best as support.")

        # create character by getting unique username
        characters = pandas.read_csv('characters.csv')
        while True:
            race = input("Which race do you want to play as? 1/2/3/4: ")
            if race == '1':
                character = Dryad(self.create_username(characters))
                race = 'dryad'
            elif race == '2':
                character = Satyr(self.create_username(characters))
                race = 'satyr'
            elif race == '3':
                character = Fury(self.create_username(characters))
                race = 'fury'
            elif race == '4':
                character = Naiad(self.create_username(characters))
                race = 'naiad'
            else:
                print("Invalid input. Please type 1/2/3/4.")
                continue
            break
        # save new character to characters.csv
        characters.loc[len(characters)] = [character.username, race, character.hp,
                                           character.x, character.y, 'elder_growth']
        characters.to_csv('characters.csv', index = False)
        return character, 'elder_growth'

    """
    build_character method
    creates a character from saved data
    loads current map, hp, and position
    called by load_character method
    returns character
    """
    def build_character(self, data):
        if data['race'] == 'dryad':
            character = Dryad(data['name'])
        elif data['race'] == 'satyr':
            character = Satyr(data['name'])
        elif data['race'] == 'fury':
            character = Fury(data['name'])
        elif data['race'] == 'naiad':
            character = Naiad(data['name'])
        else:
            print('There was an error with the character data.')
            print('Unable to load character.')
            quit()
        character.x = data['x']
        character.y = data['y']
        character.hp = data['hp']
        return character

    """
    load_character method
    displays saved characters from a csv file
    user chooses which character to play as
    returns the loaded character and current map
    """
    def load_character(self):
        characters = pandas.read_csv('characters.csv')
        #characters = pandas.read_csv(file_path)
        # list available characters from dataframe
        print('Available characters:')
        for index, c in characters.iterrows():
            print(f"{c['name']:10} : {c['race']}")
        # prompt for a name choice until a suitable string is typed
        while True:
            name = input("Type the name of the character you would like to play: ")
            match = False
            for index, c in characters.iterrows():
                if name == c['name']:
                    match = True
                    c_data = c
                    mname = c_data['current map']
                    return self.build_character(c_data), mname
            if not match:
                print('That name does not match any of the characters listed.')
                print('Check spelling and capitalization.')

    """
    save_character method
    takes current character data and saves it to a csv file
    """
    def save_character(self, player, cmap):
        characters = pandas.read_csv('characters.csv')
        # create variable for race
        if isinstance(player, Dryad):
            race = 'dryad'
        elif isinstance(player, Satyr):
            race = 'satyr'
        elif isinstance(player, Fury):
            race = 'fury'
        elif isinstance(player, Naiad):
            race = 'naiad'
        # create variable for map name
        for index, row in cmap.spaces.iterrows():
            if row['x'] == 0 and row['y'] == 0:
                mname = row['to']
        # update dataframe with current player data
        characters.loc[characters['name'] == player.username] = [player.username, race, player.hp,
                                                                 player.x, player.y, mname]
        # save updated dataframe to csv file
        characters.to_csv('characters.csv', index = False)

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
        # create Map from dataframe
        current_map = Map(mname)
        # display current map name and entities with their respective positions
        print(f'\nLoading map... {current_map.spaces.iloc[0]['space type']}\n')
        for e in current_map.entities:
            print(e)

        # player action cycle - player action, mob actions, passive abilities
        while True:
            # player chooses an action
            action = (input("\nChoose an action (or 'x' to exit to menu): "))
            # move action
            if action.lower() == 'w' or action.lower() == 'a' or action.lower() == 's' or action.lower() == 'd':
                current_map = self.move(action, player, current_map)
            # attack action
            elif action.lower() == 'i' or action.lower() == 'j' or action.lower() == 'k' or action.lower() == 'l':
                pass
            # interact action
            elif action.lower() == 'n':
                self.check_interact(player, current_map)
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
                self.save_character(player, current_map)
                break
            # buttons that don't do anything
            else:
                print("Command had no effect.")
                continue

            # mobs would act here

            # use innate ability if appropriate
            player.innate_ability(current_map.get_space_type(player.x, player.y))
            # rejuvenate if at Elder Growth 8,8
            if player.x == 8 and player.y == 8 and current_map.spaces.iloc[0]['space type'] == 'Elder Growth':
                player.rest()
            # display status if there is one
            if player.status != 'none':
                print(f'Your current status is {player.status}')

"""
main method
runs the game's main menu, in which the user can
1) run the game, which is done through Arete's run_game method
2) create a character through Arete's character creation methods
3) load a previously made/played character from a csv file
4) view the stats of the character they've created/loaded
5) view the controls if they're unsure how to play, or
x) exit the program
"""
def main():
    game = Arete()
    print("\nWelcome, hoplite, to Arete: a game inspired by Greek mythology!")

    #Main Menu
    while True:
        print("\nMain Menu")
        print("1. Play")
        print("2. Create New Character")
        print("3. Load Character")
        print("4. View Character Stats")
        print("5. View Controls")
        print("x. Quit Game")
        choice = input("Choose an operation: ")

        # Launch game
        if choice == '1':
            if 'player' in locals():
                # launch game
                game.run_game(player, mname)
            else:
                print("You haven't chosen a character yet.")
                print("You need to create or load a character before you can play.")
        # Create a new character
        elif choice == '2':
            player, mname = game.create_character()
        # Load a preexisting character
        elif choice == '3':
            player, mname = game.load_character()
        # View character stats
        elif choice == '4':
            if 'player' in locals():
                print(player)
            else:
                print("You haven't chosen a character yet.")
                print("You need to create or load a character"
                      " before you can view their stats.")
        # View the gameplay controls
        elif choice == '5':
            print("----------------------------------------------------------------------------")
            print(" move       fight    race abilities     interact      view stats       quit")
            print("----------------------------------------------------------------------------")
            print("W A S D    I J K L       Q   E             N              P              X")
            print("------------^-^-^-----------------------------------------------------------")
            print("      main hand lowercase / off hand uppercase")
        elif choice == 'x':
            break
        else:
            print("Invalid input!")
            print("Please type a number between 1 and 5, or x to exit.")


if __name__ == "__main__":
    main()