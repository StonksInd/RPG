from gears.weapon import Weapons
from gears.armor import Armor
from characters.character import Character
from random import randint

class Ennemi(Character):
    
    def __init__(self,
                 name_perso : str,
                 hp_basic : int,
                 armor : Armor,
                 weapon : Weapons,
                 type : str,
                 mana_basic : int = 0
                 
                 
                 ):
        
        
        self.name_perso= name_perso
        self.hp_basic = hp_basic
        self.armor = armor
        self.weapon = weapon
        self.mana_basic = mana_basic
        self.type = type 

    def __str__(self):
        return self.name_perso
    
    def get_mana(self) -> int:
        return (self.weapon.mana + self.mana_basic)
    
    
    def recup_mana(self):
        self.mana_basic += randint(10, 50)
        return self.mana_basic

    def recup_hp(self):
        self.hp_basic += randint(20, 60)
        return self.hp_basic

    def return_type(self):
        return self.type
