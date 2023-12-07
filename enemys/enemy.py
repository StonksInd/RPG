from gears.weapon import Weapons
from gears.armor import Armor
class Enemy:
    
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