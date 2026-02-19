"""
Author: Jasmine Frye
Program: Mythos game (name is a placeholder)
Vision: open-world MMO without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
InanimateObject class
"""


"""
Entity class
Parent class for all nonplayer entities found on maps
At this point, simply verifies that the object exists
"""

class Entity:
    def __init__(self, xy, name):
        self.x = xy[0]
        self.y = xy[1]
        self.name = name

    def __repr__(self):
        return f"{self.name} - position: {self.x},{self.y}"

    def interact(self):
        print(f"You've encountered {self.name}.")

"""
Inanimate class
Shell for inanimate objects found on maps
At this point, simply verifies that the object exists
"""

class Inanimate(Entity):
    def __init__(self, xy, name):
        super().__init__(xy, name)

    def __repr__(self):
        return f"Inanimate: {self.name} - position: {self.x}, {self.y}"

    def interact(self):
        super().interact()

"""
Npc class
Shell for nonplayer characters found on maps
At this point, simply verifies that the npc exists
"""

class Npc(Entity):
    def __init__(self, xy, name):
        super().__init__(xy, name)

    def __repr__(self):
        return f"Npc: {self.name} - position: {self.x}, {self.y}"

    def interact(self):
        super().interact()

"""
Mob class
Shell for nonplayer mobs found on maps
At this point, simply verifies that the mob exists
"""

class Mob(Entity):
    def __init__(self, xy, name, status):
        super().__init__(xy, name)
        if status == "hostile":
            self.hostile = True
        elif status == "friendly":
            self.hostile = False

    def __repr__(self):
        if self.hostile:
            return f"{self.name} - position: {self.x}, {self.y}. {self.name} is hostile."
        else:
            return f"{self.name} - position: {self.x}, {self.y}. {self.name} is friendly."

    def interact(self):
        super().interact()
        if self.hostile:
            print(f"This {self.name} might be dangerous.")