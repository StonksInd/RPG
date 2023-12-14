from gears.weapon import Weapons
from gears.armor import Armor
from characters.mage import Mage

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
    
    
    
        
    def dammage_reduction(self, dammage) -> int:
        armor = self.armor.armor
        self.hp_basic -= ((1-(armor/500)) * dammage)
        self.hp_basic = int(self.hp_basic)
        return self.hp_basic
        
    def magic_dammage_reduction(self, magic_dammage) -> int:
        magic_resistance = self.armor.magic_resistance
        self.hp_basic -= ((1-(magic_resistance/500)) * magic_dammage)
        self.hp_basic = int(self.hp_basic)
        return self.hp_basic
        
    def damage_returned(self, dammage) -> int:
        thorns = self.armor.thorns
        self.hp_basic -= ((1-(thorns/500)) * dammage)
        self.hp_basic = int(self.hp_basic)
        return self.hp_basic
    
    def get_mana(self) -> int:
        return (User_1.weapon.mana + self.mage.mana_basic)

    def choose_attack(self) -> float:
        choice = None
        while True:
            choice = str(input("Quelle attaque voulez-vous utiliser ?"))
            for x in self.get_mana():
                if self.mana >= x.cost:
                    canAttack = True