from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapons
from random import randint

class Barbarian(Character):
    
    
    def __init__(self,
                 name_perso : str,
                 armor: Armor,
                 weapon : Weapons,
                 hp_basic : int = 200,
                 name_classe : str = "Barbarian",                 
                 ):
        
        
        self.name_perso = name_perso
        self.name_classe = name_classe
        self.hp_basic = hp_basic
        self.weapon = weapon
        self.armor = armor
        
        
    def recup_hp(self):
        self.hp_basic += randint(20, 60)
        return self.hp_basic        
        

            

    
