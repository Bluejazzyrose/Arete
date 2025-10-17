## Arete
### Greek Mythology MMORPG

Date started: October 2024

The grand vision for Arete—named for the Greek word meaning excellence, integrity, or virtue—is an MMO game with two unique mechanics. First, unlike most MMOs, the player does not progress through the game via leveling, which is tedious and makes certain aspects of the game inaccessible until you have played for long enough. Second, each type of character the player can make has unique death mechanics; the player doesn’t just respawn at a specific place when they die. Visually, the game would be somewhat top-down, using a grid-like map structure, with small maps that the player can traverse seamlessly between.

Algorithm:
* Four unique race classes that the player can choose between, each with unique abilities and death mechanics, which are subclasses of a single parent class Player
* Many unique maps that the player can seamlessly traverse between
    * Different terrain types: squares that are blocked, aquatic spaces, outdoor spaces, etc., which do different things depending on the player’s character race.
    * Unique objects populate each map, which the player can interact with depending on the object type
* File interaction
    * Player inventory
    * Progress save capabilities
* Pygame and GUI to manage game animated graphics

Progress Report:
1. So far I’ve created and tested the Player class, and the four derived classes Dryad, Satyr, Fury, and Naiad. I also created a class called Mythos to handle gameplay methods, and separated main, Mythos, and the individual Player Classes into separate py files, with the Player-related files stored in their own package. I wrote a user interface menu in main, and have started working on the map logic using csv files. I am having difficulty getting that to work, but I’m sure I’ll figure it out, or find a reference for someone who did.
2. Of course the thing causing difficulty with the maps for three weeks was an erroneous comma. With that fixed, the map logic now functions. The player’s position changes accordingly with the map shift. I’ve also fixed the logic for inanimate objects, npcs, and mobs, so that the player can interact with objects on the map if they share a space. Eventually I’d like to add inventory capabilities, which would allow for quests in the future. For the file interaction requirement, I’ll either mess with inventory or add character/map position saving capabilities so you don’t start over every time you play.
3. For the file manipulation requirement, instead of doing player inventory, I have added a csv file to handle character save capabilities. The program will save a character, including their current xy position, current map, and current hp when the character is created, and will update the data in the csv to reflect play changes when the user exits the game. There is verification to prevent multiple characters with the same name so that there are no issues retrieving data from the csv file.