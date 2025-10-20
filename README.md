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
3. I have added a csv file to handle character save capabilities. The program will save a character, including their current xy position, current map, and current hp when the character is created, and will update the data in the csv to reflect play changes when the user exits the game. There is verification to prevent multiple characters with the same name so that there are no issues retrieving data from the csv file.

References for Python:
* [How to check if a variable exists](https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists)
* [Formatting print statements](https://docs.python.org/3/tutorial/inputoutput.html)
* [Turning Python code into a .exe file](https://www.geeksforgeeks.org/python/convert-python-script-to-exe-file/)
* Lists
    * [How to remove items](https://www.geeksforgeeks.org/how-to-remove-an-item-from-the-list-in-python/)
    * [Finding an item's index](https://www.geeksforgeeks.org/python-list-index/)
* Pandas Dataframes
    * [Update column value](https://www.geeksforgeeks.org/update-column-value-of-csv-in-python)
    * [Filter rows by multiple column values](https://saturncloud.io/blog/how-to-use-pandas-to-check-multiple-columns-for-a-condition/#:~:text=to%20switch%20tools.-,Using%20the%20loc%20Method%20to%20Filter%20Rows%20Based%20on%20Multiple,operators%20to%20combine%20multiple%20conditions.)
    * [Update column values based on a condition](https://datascience.stackexchange.com/questions/58232/conditional-statement-to-update-columns-based-on-range)
    * [Iterate over rows in a dataframe](https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/)
    * [Saving a dataframe to a csv file](https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/)
    * [Add a row to a dataframe](https://www.geeksforgeeks.org/how-to-add-one-row-in-an-existing-pandas-dataframe/)
    * [Update row values based on a condition](https://saturncloud.io/blog/how-to-update-values-in-a-specific-row-in-a-python-pandas-dataframe/#:~:text=Updating%20a%20single%20value%20in%20a%20row,-Let's%20start%20with&text=We%20can%20use%20the%20.,desired%20column%20using%20the%20%3D%20operator.)
    * [Delete 1 row from a dataframe/CSV](https://www.geeksforgeeks.org/how-to-delete-only-one-row-in-csv-with-python/)
* PyGame
    * [Basic Tutorial](https://www.geeksforgeeks.org/python/pygame-tutorial/)
    * [Walkthrough Introduction](https://www.geeksforgeeks.org/python/introduction-to-pygame/)
    * [Creating a Menu](https://www.geeksforgeeks.org/python/create-settings-menu-in-python-pygame/)
* Flask
    * [Flask tutorial](https://www.geeksforgeeks.org/flask-tutorial/)
    * [Flask Basic Tutorial](https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/)
    * [Flask TicTacToe Game Tutorial](https://www.youtube.com/watch?v=qSAFEV-k_Fk)
    * [Passing js variables to Python and back using Flask](https://www.geeksforgeeks.org/pass-javascript-variables-to-python-in-flask/)
* HTML, JavaScript, & CSS
    * [Web-safe Fonts](https://www.w3schools.com/cssref/css_websafe_fonts.php)
    * [Fill a grid using Javascript and/or CSS](https://stackoverflow.com/questions/57550082/creating-a-16x16-grid-using-javascript)
    * [Make a div that scrolls vertically](https://www.geeksforgeeks.org/making-a-div-vertically-scrollable-using-css/)
    * [Get & post](https://healeycodes.com/talking-between-languages)

References for Greek Mythology:
* [Locations in Greek mythology](https://www.greekmythology.com/Myths/Places/places.html)
* [Plutus, Greek god of agricultural bounty](https://www.theoi.com/Georgikos/Ploutos.html)
* [Greek monsters and other creatures](https://en.m.wikipedia.org/wiki/List_of_Greek_mythological_creatures)