from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapons

class Mage(Character):
    
    
    def __init__(self,
                 name_perso : str,
                 armor: Armor,
                 weapon : Weapons,
                 hp_basic : int = 100,
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
        

    def get_mana(self) -> int:
        return (self.weapon.mana + self.mana_basic)
    
    def attaque_magique(self, niveau_de_sort):#permet de différencier les sort lvl 1 et 2 ect... et de conso le mana de l'attack
        cout_mana_spell = 20*niveau_de_sort
        return cout_mana_spell
 


    
    
