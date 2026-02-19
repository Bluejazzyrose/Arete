"""
Author: Jasmine Frye
Program: Arete game
Vision: open-world MMORPG without leveling crawl, inspired by Greek mythology
Prominent feature: unique death mechanics, not just 'respawn'
Player race parent and child classes
"""

class Player:
    def __init__(self, char_dict):
        self.username = char_dict["name"]
        self.position = char_dict["position"]
        self.spd = 1
        self.status = None
        # inventory logic will go here in future iterations

    def one_ability(self):
        pass
    def two_ability(self):
        pass
    def innate_ability(self, space_type):
        pass
    def rest(self):
        print('All stats and abilities have been reset to original values and status.')
        self.status = 'none'

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
Dryad Plant Class
For plant entities that the dryad creates
Might move this class to entities.py
"""
class DryadPlant:
    def __init__(self, x, y, is_tree):
        #position on map
        self.x = x
        self.y = y
        #tree or shrub
        self.is_tree = is_tree


"""
Dryad Character Class
Self-healing and crowd control abilities
Dryad plants can benefit Satyrs
"""
class Dryad(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 50  # max hp is 50
        self.race = "Dryad"
        self.photosynthesis = 0
        self.dryad_plants = []

    def __repr__(self):
        return f"{self.username} - race: Dryad, max hp: 50 ({self.hp} remaining)."

    """
    X / E: grappling vines
    3x3 AoE, 10 move cooldown
    ROOTS non-flying entities for 5 moves
    """
    def one_ability(self):
        pass

    """
    Y / Q: healing shrub
    heal 5 hp; places a DryadPlant shrub
    Satyrs can eat shrub for same effect
    Photosynthesis is set back to monitor frequency of use
    """
    def two_ability(self):
        if self.photosynthesis > -1:
            #place dryad shrub at current position
            self.dryad_plants.append(DryadPlant(self.x, self.y, False))

            #heal 5 hp
            if self.hp < 45:
                self.hp += 5
            elif self.hp < 50:
                self.hp = 50

            #set back photosynthesis to monitor frequency of use
            self.photosynthesis = -10

    """
    innate_ability: photosynthesis
    every 10 outdoor spaces traversed increases current hp by 1, to max
    if on outdoor space, increase photosynthesis
    """
    def innate_ability(self, space_type):
        if space_type == 'outdoor':
            self.photosynthesis += 1
        if self.photosynthesis > 9 and self.hp < 50:
            self.hp += 1
            self.photosynthesis = 0
            print("You've healed 1 hp via photosynthesis!")

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 50
        self.photosynthesis = 0


"""
Satyr Character Class
Abilities with high mobility and horns that damage attackers
Can regain hp by eating Dryad plants
"""
class Satyr(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 25  # max hp is 25
        self.race = "Satyr"
        self.bound = 10  # max bound is 10
        self.is_bounding = False

    def __repr__(self):
        return f"{self.username} - race: Satyr, max hp: 25 ({self.hp} remaining)."

    """
    interact method override: eat dryad plants
    In addition to interacting with normal objects,
    Satyrs can also interact with plants left by Dryads
    """
    def check_heal(self, interactee):
        healed = False
        if isinstance(interactee, DryadPlant):
            healed = True
            if interactee.is_tree:
                if self.hp < 15:
                    self.hp += 10
                elif self.hp < 25:
                    self.hp = 25
                else:
                    healed = False
            else:
                if self.hp < 20:
                    self.hp += 5
                elif self.hp < 25:
                    self.hp = 25
                else:
                    healed = False
        return healed

    """
    X / E: Head Charge
    charge in the direction faced until you hit a wall
    pinned enemies take 5 dmg
    """
    def one_ability(self):
        pass

    """
    Y / Q: Bound
    move 2x speed for up to 30 seconds
    toggles the ability on or off depending what the current status is
    and adjusts the speed accordingly
    """
    def two_ability(self):
        if not self.is_bounding:
            self.is_bounding = True
            self.spd = 2
        else:
            self.is_bounding = False
            self.spd = 1

    """
    innate_ability: Sharp Horns
    deal 2 dmg to any mobs in the same space
    # add logic in Mythos: check space for mobs after each action
    # no logic for this in Satyr??
    
    innate_ability logic progresses and monitors bound
    if two_ability is off, increase bound per space to max
    if two_ability is on, decrease bound per space to 0
    """
    def innate_ability(self, space_type):
        if not self.is_bounding and self.bound < 10:
            self.bound += 1
        elif self.bound > 0:
            self.bound -= 1
        else:
            self.two_ability()

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 25
        self.bound = 10
        self.is_bounding = False


"""
Fury Character Class
Steals health from allies
Spends health to deal massive damage
"""
class Fury(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 10    #max hp is 10
        self.race = "Fury"
        self.friendly_fire = False
        self.kindled_on = False
        self.kindling = 0
    def __repr__(self):
        return f"{self.username} - race: Fury, max hp: 10 ({self.hp} remaining)."

    """
    X / E: Kindled Fury
        or Scream if 0 hp
    """
    def one_ability(self):
        if self.kindled_on:
            self.kindled_on = False
            self.hp -= self.kindling
            self.kindling = 0
        else:
            self.kindled_on = True

    """
    Y / Q: Friendly Fire
    """
    def two_ability(self):
        if self.friendly_fire:
            self.friendly_fire = False
        else:
            self.friendly_fire = True

    """
    innate_ability: track ghostly status and kindling
    if the fury runs out of hp, set status to ghostly
    if kindled fury is activated, progress kindling
    """
    def innate_ability(self, space_type):
        # check if status should be ghostly
        if self.hp < 1:
            self.status = 'ghostly'
            self.hp = 0
        elif self.hp > 9 and self.status == 'ghostly':
            self.status = 'none'
        # progress kindling if kindled fury is activated
        elif self.kindled_on:
            if self.kindling < 10:
                self.kindling += 1
            if self.kindling > 9:
                print('Maximum potency for Kindled Fury has been reached.')
                print('Release now to deal massive damage.')
            print(f'Current damage potential is {self.kindling * self.kindling}.')

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 10
        self.friendly_fire = False
        self.kindled_on = False
        self.kindling = 0


"""
Naiad Character Class
Self-healing and crowd control abilities
Good at evading damage
"""
class Naiad(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 25    #max hp is 25
        self.race = "Naiad"
        self.aqua = 0
        self.puddle = False

    def __repr__(self):
        return f"{self.username} - race: Naiad, max hp: 25 ({self.hp} remaining)."

    """
    X / E: Create Puddle
    """
    def one_ability(self):
        return [[self.x, self.y],[self.x, self.y - 1],[self.x, self.y + 1],
                [self.x - 1, self.y],[self.x - 1, self.y - 1],[self.x - 1, self.y + 1],
                [self.x + 1, self.y],[self.x + 1, self.y - 1],[self.x + 1, self.y + 1],]

    """
    Y / Q: Become Puddle
    FUTURE: pause every other function, including healing and taking damage
    """
    def two_ability(self):
        if self.puddle:
            self.puddle = False
        elif not self.puddle:
            self.puddle = True
        print(f"Now in puddle form: {self.puddle}.")

    """
    innate_ability: Aquatic Regeneration
    every 5 aquatic spaces traversed increases current hp by 1, to max
    added logic in Mythos: if on aquatic space, increase aqua
    """
    def innate_ability(self, space_type):
        if space_type == 'aquatic' and not self.puddle:
            self.aqua += 1
        if self.aqua > 4 and self.hp < 25:
            self.hp += 1
            self.aqua = 0
            print("You've healed 1 hp via aquatic regeneration!")

    """
    rest: reset all stats to original status
    """
    def rest(self):
        super().rest()
        self.hp = 25
        self.aqua = 0
        self.puddle = False