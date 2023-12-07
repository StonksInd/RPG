from character import Character
from armor import Armor
from weapon import Weapons

class Barbarian(Character):
    
    
    def __init__(self,
                 name_perso : str,
                 armor: Armor,
                 weapon : Weapons,
                 hp_basic : int,
                 name_classe : str = "Barbarian",
                 nb_attack : int = 2,
                 
                 ):
        
        
        self.name_perso = name_perso
        self.name_classe = name_classe
        self.nb_attack = nb_attack
        self.hp_basic = hp_basic
        self.weapon = weapon
        
 
            

    
