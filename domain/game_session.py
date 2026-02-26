"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race classes and maps are imported from separate files
"""

from map import Map


class GameSession:
    def __init__(self, player, map_name):
        self.player = player
        self.map = Map(map_name)
        self.running = True

    def run(self):
        print(f"\nLoading map... {self.map.name}\n")
        self.map.describe_entities()

        while self.running:
            action = input("Choose action: ").lower()
            self.handle_action(action)
            self.process_turn()

    def handle_action(self, action):
        if action in ['w','a','s','d']:
            self.player.move(action, self.map)

        elif action == 'n':
            self.player.interact(self.map)

        elif action == 'e':
            self.player.one_ability(self.map)

        elif action == 'q':
            self.player.two_ability(self.map)

        elif action == 'p':
            print(self.player)

        elif action == 'x':
            self.running = False

        else:
            print("Command had no effect.")

    def process_turn(self):
        self.map.update_entities(self.player)
        self.player.process_passives(self.map)