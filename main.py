from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from enemys.enemy import Ennemi
from random import randint
from gears.spell import Spell
from arena import Arena

#armes physique


# classe = [Mage, Barbarian]
# armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
# weapon = [La_main, Massue, Lance, Hache, Baton, Baguette, Sceptre]
# spell = [Etincelle,Boule_de_feu, Vague_tonante]
# ennemie_physique= [Gobelin, Hobogoblin, Orc, Ogre]
# ennemie_magique =[Salamendre_elementaire, Sorciere, Golem_magique, Elentaire]
# classe_choisie, armor_choisie, weapon_choisie, difficulte_choisie = len(classe), len(armor), len(weapon), len(ennemie_physique)

# def send_name(tab):
#     str_return = ""
#     for i in range (len(tab)):
#         str_return += str(i) + ":" + str(tab[i])+ ", "
#     return str_return



# name_user = str(input("quel est votre nom ? : "))
# while classe_choisie < 0 or classe_choisie > len(classe)-1:
#     classe_choisie = int(input(f"veuillez entrer votre classe 0:Mage, 1:Barbarian "))
# while armor_choisie <0 or armor_choisie > len(armor)-1:
#     armor_choisie = int(input(f"quelle armure voulez vous {send_name(armor)} "))
# while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
#     weapon_choisie = int(input(f"quelle arme voulez vous {send_name(weapon)} "))
# while difficulte_choisie < 0 or difficulte_choisie > len(ennemie_magique)-1:
#     difficulte_choisie = int(input("quelle difficulté voulez vous ? la 1, 2, 3 ou 4 ")) -1

# ennemie = [ennemie_physique[difficulte_choisie],ennemie_magique[difficulte_choisie]]
# User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])

# print("--------------------------------------")
# print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
# print(f"Vous avez choisi {User_1.name_classe} comme classe, elle à {User_1.hp_basic} point de vie")
# print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} d'armure, {User_1.armor.magic_resistance} d'armure magique et {User_1.armor.thorns} de thorns. ")
# print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégats, {User_1.weapon.magic_damage} dégat magique, donne {User_1.weapon.mana} mana et donne {User_1.weapon.armor_weapon} points d'armures.")


input_us = input("quel mode voulez vous jouer ? : fight (un 1vs1) / adventure(le mode histoire)")
if input_us == "fight":
    Arena.fight()
    
    
if input_us == "adventure":
    Arena.adventure()
    
            
            

#! mettre en place arena avec un clean du main en cours



#! Classe arena 

#? Bonus
#?Carte et salle 
#? pouvoir utiliser 2 personnage en mode campagne (en multi quoi)
