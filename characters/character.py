from gears.weapon import Weapons
from gears.armor import Armor

class Character:
    
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
        
    def prendre_degats(self, degats):
        self.hp_basic -= degats
        if self.hp_basic <= 0:
            self.hp_basic = 0
            print(f"{self.name_perso} a été vaincu!")

        
        

    
        
      
        
