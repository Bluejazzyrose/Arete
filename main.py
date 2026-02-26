"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Main py file
"""

from domain.load_races import load_all_races

def main():
    load_all_races()
    print("Hi! No problems here!")

if __name__ == "__main__":
    main()