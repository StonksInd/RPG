from gears.weapon import Weapons
from gears.armor import Armor
from random import randint

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
        
    # def prendre_degats(self, degats):
    #     self.hp_basic -= degats
    #     print(self.armor.armor)
    #     if self.hp_basic <= 0:
    #         self.hp_basic = 0
    #         print(f"{self.name_perso} a été vaincu!")
    
    
    
        
    def dammage_reduction(self, dammage, other) -> int:
        armor = self.armor.armor
        crit_esquive = randint(0,101)
        if crit_esquive <= 5:
            print("vous avez fait un critique")
            self.hp_basic -= ((1-(armor/500)) * (dammage *1.5))
        if crit_esquive >=95:
            print(f"{self.name_perso} esquive l'attaque énemie")
            return self.hp_basic 
        else:
            self.hp_basic -= ((1-(armor/500)) * dammage)
            other.hp_basic -= ((1-(other.armor.armor/500)) * self.armor.thorns)
            print(f"vous avez infligé {int(((1-(armor/500)) * dammage))}")
        self.hp_basic = int(self.hp_basic)
        other.hp_basic = int(other.hp_basic)
        return self.hp_basic, other.hp_basic
    
        
    def magic_dammage_reduction(self, magic_dammage, other) -> int:
        magic_resistance = self.armor.magic_resistance
        self.hp_basic -= ((1-(magic_resistance/500)) * magic_dammage)
        self.hp_basic = int(self.hp_basic)
        print(f"vous avez infligé {int(((1-(armor/500)) * dammage))}")
        return self.hp_basic
        
    def damage_returned(self, dammage) -> int:
        thorns = self.armor.thorns
        self.hp_basic -= ((1-(thorns/500)) * dammage)
        self.hp_basic = int(self.hp_basic)
        return self.hp_basic
