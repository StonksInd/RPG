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
        
    # def prendre_degats(self, degats):
    #     self.hp_basic -= degats
    #     print(self.armor.armor)
    #     if self.hp_basic <= 0:
    #         self.hp_basic = 0
    #         print(f"{self.name_perso} a été vaincu!")
    
    

            
    def dammage_reduction(self, dammage, other) -> int:
        armor = self.armor.armor + self.weapon.armor_weapon
        crit_esquive = randint(0,101)
        
        
        if crit_esquive <= other.weapon.taux_crit_weapon:
            print("vous avez fait un critique")
            self.hp_basic -= ((1-(armor/500)) * (dammage *1.5))
            
        if crit_esquive >=95:
            print(f"{self.name_perso} esquive l'attaque énemie")
            return self.hp_basic 
        
        else:
            self.hp_basic -= ((1-(armor/500)) * dammage)
            other.hp_basic -= ((1-(other.armor.armor/500)) * self.armor.thorns)
            print(f"l'armure de {other.name_perso} vous inflige {int((1-(other.armor.armor/500)) * self.armor.thorns)}")
            print(f"{self.name_perso} a infligé {int(((1-(armor/500)) * dammage))} a {otehr.name_perso} ")
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
            print(f"{self.name_perso} esquive l'attaque énemie")
            return self.hp_basic 
        
        else:
            self.hp_basic -= ((1-(magic_resistance/500)) * (magic_dammage * spell_a_lancer.spell_dammage))
            other.mana_basic -= spell_a_lancer.mana_cost
            print(f"vous avez infligé {int(((1-(magic_resistance/500)) * (magic_dammage *spell_a_lancer.spell_dammage)))}")
        self.hp_basic = int(self.hp_basic)
        
        return self.hp_basic, other.mana_basic
        

        

