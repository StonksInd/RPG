from gears.weapon import Weapons
from gears.armor import Armor
from characters.character import Character
class Enemy(Character):
    
    def __init__(self,
                 name_perso : str,
                 hp_basic : int,
                 armor : Armor,
                 weapon : Weapons,
                 
                 ):
        
        
        self.name_perso= name_perso
        self.hp_basic = hp_basic
        self.armor = armor
        self.weapon = weapon