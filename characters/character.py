from gears.weapon import Weapons
from gears.armor import Armor
from gears.spell import Spell
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
        

            
    def dammage_reduction(self, dammage, other) -> int:
        armor = self.armor.armor + self.weapon.armor_weapon
        crit_esquive = randint(0,101)
        
        
        if crit_esquive <= other.weapon.taux_crit_weapon:
            print("vous avez fait un critique")
            self.hp_basic -= ((1-(armor/500)) * (dammage *1.5))
            
        if crit_esquive >=95:
            print(f"{self.name_perso} esquive l'attaque énnemie")
            return self.hp_basic 
        
        else:
            self.hp_basic -= ((1-(armor/500)) * dammage)
            other.hp_basic -= ((1-(other.armor.armor/500)) * self.armor.thorns)
            print(f"{other.name_perso} a infligé {int(((1-(armor/500)) * dammage))} dégats à {self.name_perso} ")
            print(f"l'armure de {self.name_perso} inflige {int((1-(other.armor.armor/500)) * self.armor.thorns)} dégats de thorns à {other.name_perso}")
        self.hp_basic = int(self.hp_basic)
        other.hp_basic = int(other.hp_basic)
        return self.hp_basic, other.hp_basic
    
        
    def magic_dammage_reduction(self, magic_dammage, spell_a_lancer, other) -> int:
        magic_resistance = self.armor.magic_resistance
        crit_esquive = randint(0,101)
        
        if crit_esquive <= 5:
            print("vous avez fait un critique")
            self.hp_basic -= ((1-(magic_resistance/500)) * ((magic_dammage * spell_a_lancer.spell_dammage)* 1.5))
            print(f"vous avez infligé {int(((1-(magic_resistance/500)) * ((magic_dammage *spell_a_lancer.spell_dammage* 1.5))))}")
            other.mana_basic -= spell_a_lancer.mana_cost
            
            
        if crit_esquive >=95:
            print(f"{self.name_perso} esquive l'attaque énnemie")
            return self.hp_basic 
        
        else:
            self.hp_basic -= ((1-(magic_resistance/500)) * (magic_dammage * spell_a_lancer.spell_dammage))
            other.mana_basic -= spell_a_lancer.mana_cost
            print(f"{other.name_perso} infligé {int(((1-(magic_resistance/500)) * (magic_dammage *spell_a_lancer.spell_dammage)))} à {self.name_perso}")
        self.hp_basic = int(self.hp_basic)
        
        return self.hp_basic, other.mana_basic
        

        

