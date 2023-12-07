

class Armor:
    def __init__(self,
                 name_armor: str,
                 armor : int,
                 thorns : int,
                 magic_resistance : int,
                 ):
        self.name_armor = name_armor
        self.armor = armor
        self.thorns = thorns
        self.magic_resistance = magic_resistance

def get_armor(self) -> int:
    return (self.armor + self.Armor.get_armor())
    
def dammage_reduction(self, dammage) -> int:
    armor = self.get_armor()
    return ((self.hp_basic)-((1-(armor/500)) * dammage))
    
def get_magic_resistance(self) -> int:
    return (self.magic_resistance + self.Armor.get_magic_resistance())
    
def magic_dammage_reduction(self, magic_dammage) -> int:
    magic_resistance = self.get_magic_resistance()
    return ((self.hp_basic)-((1-(magic_resistance/500)) * magic_dammage))