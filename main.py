from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from enemys.enemy import Enemy

no_weapon = Weapons("No Weapon", 0, 0, 0, 0)
weapon_hivemind = Weapons("Hivemind", 25, 0, 0, 0)
weapon_songsteel = Weapons("Songsteel", 20, 0, 0, 15)
weapon_riftmaker = Weapons("Riftmaker", 0, 25, 100, 0)

no_armor = Armor("No Armor", 0, 0, 0)
armor_warmog = Armor("Warmog", 100, 0, 0)
armor_thornmail = Armor("Thornmail", 60, 25, 0)
 
def choose_all():
    choose_character = input("Choisissez votre classe entre Barbarian, Mage")
    if choose_character == "Barbarian":
        choose_weapon = input('Choisissez votre arme entre')
        choose_armor = input('Choisissez l/armure entre ')
        choose_name = str(input('Choisissez votre nom :'))
        
        
        
        
Michel = Enemy("Slip", 100, armor_warmog, weapon_hivemind)
francois = Mage("jean", no_armor, weapon_hivemind, 100)

def choose_attack(self) -> int:
    while True:
        input_user = str(input("veuillez entrer votre action : "))
        if input_user.lower() == "quitter":
            canAttack = False
            print("vous quitez le jeu")
            break
        if input_user.lower() == "attaquer":
            for x in self.get_mana():
                    if self.mana >= x.cost():
                        canAttack = True
            Michel.dammage_reduction(francois.weapon.dammage)
            print(f"vous attaquer l'enemy de {francois.weapon.dammage} ")
        if canAttack:
            return Michel.hp_basic
        else : 
            print("Vous n'avez pas assez de mana")
 



# print(francois.weapon.dammage) 
      


# print(Michel.weapon.dammage) 

# Michel.weapon.degats(francois)
# print(Michel.weapon.degats(francois))
# print(francois.hp_basic)
Michel.armor.thorns