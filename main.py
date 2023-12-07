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
        

def affichage():
    while True:
        input_user = str(input("veuillez entrer votre action : "))
        if input_user.lower() == "quitter":
            print("vous quitez le jeu")
            break
affichage()


francois = Mage("jean", no_armor, no_weapon, 100)
print(francois.weapon.dammage) 
      

Michel = Enemy("Slip", no_armor, no_weapon, 100)
print(Michel.weapon.dammage) 