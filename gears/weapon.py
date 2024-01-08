
class Weapons:
    def __init__(self,
                 name_weapon: str,
                 dammage : int,
                 magic_damage : int,
                 mana : int,
                 armor_weapon : int,
                 taux_crit_weapon : int = 5,
                 ):
        self.name_weapon = name_weapon
        self.dammage = dammage
        self.mana = mana
        self.magic_damage = magic_damage
        self.armor_weapon = armor_weapon
        

    def __str__(self):
        return self.name_weapon
