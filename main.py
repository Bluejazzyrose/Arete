"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""


import pandas
import os

from arete import Arete
from player_character.dryad import Dryad
from player_character.fury import Fury
from player_character.naiad import Naiad
from player_character.satyr import Satyr


"""
create_username method
prompts the user for input and returns a confirmed name choice
"""
def create_username(characters):
    while True:
        name = input("\nWhat do you want to name your character? ")
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
def create_character(character_save_file):
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
            character = Dryad(create_username(characters))
            race = 'dryad'
        elif race == '2':
            character = Satyr(create_username(characters))
            race = 'satyr'
        elif race == '3':
            character = Fury(create_username(characters))
            race = 'fury'
        elif race == '4':
            character = Naiad(create_username(characters))
            race = 'naiad'
        else:
            print("Invalid input. Please type 1/2/3/4.")
            continue
        break
    # save new character to characters.csv
    characters.loc[len(characters)] = [character.username, race, character.hp,
                                        character.x, character.y, 'elder_growth']
    characters.to_csv(character_save_file, index = False)
    return character, 'elder_growth'

"""
build_character method
creates a character from saved data
loads current map, hp, and position
called by load_character method
returns character
"""
def build_character(data):
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
def load_character(characters):
    # list available characters from dataframe
    print('\nAvailable characters:')
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
                return build_character(c_data), mname
        if not match:
            print('That name does not match any of the characters listed.')
            print('Check spelling and capitalization.')

"""
save_character method
takes current character data and saves it to a csv file
"""
def save_character(player, cmap, character_save_file):
    characters = pandas.read_csv(character_save_file)
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
    characters.to_csv(character_save_file, index = False)
    

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
    # Set up csv file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_name = "characters.csv"
    character_save_file = os.path.join(script_dir, csv_file_name)
    # Convert the csv file into a pandas dataframe
    characters = pandas.read_csv(character_save_file)

    # Define variables
    player = None
    game = Arete()
    
    #Main Menu
    print("\nWelcome, hoplite, to Arete: a game inspired by Greek mythology!")
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
            if player:
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
            if player:
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