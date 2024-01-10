from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from ennemis.ennemi import Ennemi
from random import randint
from gears.spell import Spell
from arena import Arena

input_us = ""
while input_us.lower() !="fight" and input_us.lower() != "adventure":
    input_us = input("quel mode voulez vous jouer ? : FIGHT (un 1vs1) / ADVENTURE (le mode histoire) ")
if input_us.lower() == "fight":
    Arena.fight()
    
    
if input_us.lower() == "adventure":
    Arena.adventure()
    
            
