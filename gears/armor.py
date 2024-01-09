

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
        
    def __str__(self):
        return self.name_armor
    
    

