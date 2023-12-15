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
 
        
        
Michel = Enemy("Slip", 100, armor_warmog, weapon_hivemind)
francois = Mage("jean", no_armor, weapon_hivemind, 100)


classe = [Mage, Barbarian]
armor = [no_armor, armor_warmog, armor_thornmail]
weapon = [no_weapon, weapon_hivemind, weapon_songsteel, weapon_riftmaker]

classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)

name_user = str(input("quel est votre nom ? : "))
while classe_choisie < 0 or classe_choisie > len(classe)-1:
    classe_choisie = int(input("veuillez entrer votre classe, 0: Mage, 1: Barbarian "))
while armor_choisie <0 or armor_choisie > len(armor)-1:
    armor_choisie = int(input("quelle armure voulez vous 0:no_armor, 1:armor_warmog 2:armor_thornmail "))
while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
    weapon_choisie = int(input("quelle arme voulez vous 0:no_weapon, 1:weapon_hivemind 2:weapon_songsteel 3:weapon_riftmaker "))

User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])
print("--------------------------------------")
print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
print(f"Vous avez choisi {User_1.name_classe} comme classe, elle à {User_1.hp_basic} point de vie")
print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} d'armure, {User_1.armor.magic_resistance} d'armure magique et {User_1.armor.thorns} de thorns. ")
print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégats, {User_1.weapon.magic_damage} dégat magique, donne {User_1.weapon.mana} mana et donne {User_1.weapon.armor_weapon} points d'armures.")



# while True:

#     input_user = str(input("veuillez entrer votre action : "))
#     if input_user.lower() == "quitter":
#         print("vous quitez le jeu")
#         break
#     if input_user.lower() == "attaquer":
#         if classe_choisie == 0:
#             if Michel.get_mana() <= attack: 
#                 print("Vous n'avez pas assez de mana pour attaquer")
#             else : 
#                 Michel.magic_dammage_reduction(francois.weapon.magic_damage)
#                 print(f"Vous avez infligé à l'ennemi {francois.weapon.magic_damage}")
            
#         Michel.dammage_reduction(francois.weapon.dammage)
#         print(f"vous attaquer l'enemy de {francois.weapon.dammage} ")
#         print(Michel.hp_basic)


# print(Mage.name_classe) 



# Michel.weapon.degats(francois)
# print(Michel.weapon.degats(francois))
# print(francois.hp_basic)

#todo mettre en place les combats avec une interface qui marche 
#todo mettre en place d'ifférent niveau de difficulté
#todo faire de l'aléatoire avec random qui permet de 0-5/100 de faire un critique et de 95-100/100 de louper l'attaque
#! puis mettre en places les différentes attaques pour le mage et le nb d'attaque 
#! et les dégats critiques
#! les thorns des armures




