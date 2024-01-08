

class Spell:
    
    def __init__(self,
                 spell_name : str,
                 spell_dammage : int,
                 #dot_dammage
                 mana_cost : int,
                 #porte_spell
                 
                 ):
        self.spell_name = spell_name
        self.spell_dammage = spell_dammage
        self.mana_cost = mana_cost
        
    def __str__(self):
        return self.spell_name