from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapons

class Mage(Character):
    
    
    def __init__(self,
                 name_perso : str,
                 armor: Armor,
                 weapon : Weapons,
                 hp_basic : int,
                 name_classe : str = "mage",
                 mana_basic : int = 200,
                 nb_attack : int = 1,
                 ):
        
        
        self.name_perso = name_perso
        self.armor = armor
        self.weapon = weapon
        self.name_classe = name_classe
        self.nb_attack = nb_attack
        self.mana_basic = mana_basic
        self.hp_basic = hp_basic
        
 
            

    
