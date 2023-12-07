from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons

no_weapon = Weapons("No Weapon", 0, 0, 0, 0)
weapon_hivemind = Weapons("Hivemind", 25, 0, 0, 0)
weapon_songsteel = Weapons("Songsteel", 20, 0, 0, 15)
weapon_riftmaker = Weapons("Riftmaker", 0, 25, 100, 0)

no_armor = Armor("No Armor", 0, 0, 0)
armor_warmog = Armor("Warmog", 100, 0, 0)
armor_thornmail = Armor("Thornmail", 60, 25, 0)
 


francois = Mage("jean", no_armor, no_weapon, 100)
print(francois.weapon.dammage) 
      
