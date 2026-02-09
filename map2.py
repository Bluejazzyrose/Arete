"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Map class
"""

import json
from file_paths import get_maps_file

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
        self. entities = entities

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
Map related functions not in the map object class
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


# test logic
elder_growth = load_map_by_name("grasslands", "Elder Growth")

print(elder_growth.name)
print(elder_growth.portals)
for row in elder_growth.spaces:
    print(row)
print(elder_growth.entities)