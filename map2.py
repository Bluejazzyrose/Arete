"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Map class
"""

import json
from file_paths import get_maps_file
from entities import Npc, Inanimate, Mob
from player_character.player2 import Player

"""
Map class
pulls data from a specified cvs file
keeps track of objects specific to the current map
"""
class Map:
    def __init__(self, name, portals, spaces, entities):
        self.name = name
        self.portals = portals
        self.spaces = spaces
        self.entities = [] # list to build entities in

        # build appropriate entity objects for each entry in the map data
        for e in entities:
            if e["type"] == "inanimate":
                self.entities.append(Inanimate(e["position"], e["name"]))
            elif e["type"] == "mob":
                self.entities.append(Mob(e["position"], e["name"], e["status"]))
            elif e["type"] == "npc":
                self.entities.append(Npc(e["position"], e["name"]))

    def to_dict(self):
        return {
            "name": self.name,
            "portals": self.portals,
            "spaces": self.spaces,
            "entities": self.entities
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name = data["name"],
            portals = data["portals"],
            spaces = data["spaces"],
            entities = data["entities"]
        )

    """
    Get space type method
    gets the type of the tile in question
    returns the type as a string
    """
    def get_space_type(self, coordinates: list):
        # get the char representing the tile in question
        tile_char = self.spaces[coordinates[0]][coordinates[1]]
        # return the appropriate string representing the tile type
        if tile_char == "X":
            return "impass"
        elif tile_char == "G":
            return "outdoor"
        elif tile_char == "A":
            return "aquatic"
        elif tile_char == "I":
            return "interior"
        elif tile_char == "P":
            return "portal"


"""
Map related functions not in the map object class
"""

"""
Load map by name function
accesses the appropriate maps json file
and builds a Map object from the data
"""
def load_map_by_name(file_name, map_name):
    # get the path to the appropriate map file
    file_route = get_maps_file(file_name)

    # open and load the json file into map_dicts
    with open(file_route) as f:
        map_dicts = json.load(f)

    # find the correct map in the file and objectify it 
    for map_entry in map_dicts["maps"]:
        if map_entry["name"] == map_name:
            return Map.from_dict(map_entry)

    # raise an error if the map doesn't exist
    raise KeyError(f"Map '{map_name}' not found")


"""
Change map function
handles changing the map object data
when the player moves to a portal space
returns an updated map object
"""
def change_map(m: Map, xy: list):
    # remember the last map for player placement on the new one
    last_map = m.name
    # variables to store new map identifier data
    new_map = None
    new_file = None
    # locate the name and file for the new map
    for entry in m.portals:
        if entry[0] == xy[0] and entry[1] == xy[1]:
            new_map = entry[2]
            new_file = entry[3]
            break
    # return a map with the new data
    return load_map_by_name(new_file, new_map)


"""
Move function
checks the type of the tiles being moved through/to
moves the player if the checks yield no exceptions
returns the tile type
"""
def move(m: Map, player: Player, move: list):
    # check each space in the direction moved for impass or portal spaces
    for i in range(1, player.spd + 1):
        # get the space type for the next space in the appropriate direction
        x = player.position[0] + (move[0] * i)
        y = player.position[1] + (move[1] * i)
        tile_type = m.get_space_type([x, y])

        # if there is a wall or a portal in the way, return prematurely
        # if i has reached the max distance the player can move, return
        if tile_type == "impass" or tile_type == "portal" or i == player.spd:
            if tile_type == "impass":
                print("There is an obstacle blocking your path.")
            elif tile_type == "portal":
                print("You have traversed through a portal to another map.")
            else:
                player.position = [x, y]
                print(f"You have moved to {x}, {y}.")
            return tile_type


# test logic

# test the map building function & map object
elder_growth = load_map_by_name("grasslands", "Elder Growth")

# print map details
print(elder_growth.name)
print(elder_growth.portals)
for row in elder_growth.spaces:
    print(row)
for item in elder_growth.entities:
    print(item)

# test the tile type collection function
print(get_space_type(elder_growth, [8, 8]))