from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from enemys.enemy import Enemy

no_weapon = Weapons("No Weapon", 0, 0, 0, 0)
weapon_hivemind = Weapons("Hivemind", 25, 0, 0, 0)
weapon_songsteel = Weapons("Songsteel", 20, 0, 0, 15)
weapon_riftmaker = Weapons("Riftmaker", 0, 10, 100, 0)

no_armor = Armor("No Armor", 0, 0, 0)
armor_warmog = Armor("Warmog", 100, 0, 0)
armor_thornmail = Armor("Thornmail", 60, 10, 0)

 
        
        
Michel = Enemy("Slip", 100, armor_thornmail, weapon_hivemind)
Francois = Mage("jean", armor_thornmail, weapon_riftmaker)


classe = [Mage, Barbarian]
armor = [no_armor, armor_warmog, armor_thornmail]
weapon = [no_weapon, weapon_hivemind, weapon_songsteel, weapon_riftmaker]

classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)

# name_user = str(input("quel est votre nom ? : "))
while classe_choisie < 0 or classe_choisie > len(classe)-1:
    classe_choisie = int(input("veuillez entrer votre classe, 0: Mage, 1: Barbarian "))
# while armor_choisie <0 or armor_choisie > len(armor)-1:
#     armor_choisie = int(input("quelle armure voulez vous 0:no_armor, 1:armor_warmog 2:armor_thornmail "))
# while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
#     weapon_choisie = int(input("quelle arme voulez vous 0:no_weapon, 1:weapon_hivemind 2:weapon_songsteel 3:weapon_riftmaker "))

# User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])
# print("--------------------------------------")
# print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
# print(f"Vous avez choisi {User_1.name_classe} comme classe, elle à {User_1.hp_basic} point de vie")
# print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} d'armure, {User_1.armor.magic_resistance} d'armure magique et {User_1.armor.thorns} de thorns. ")
# print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégats, {User_1.weapon.magic_damage} dégat magique, donne {User_1.weapon.mana} mana et donne {User_1.weapon.armor_weapon} points d'armures.")



while True:

    input_user = str(input("veuillez entrer votre action : "))
    if input_user.lower() == "quitter":
        print("vous quitez le jeu")
        break
    if input_user.lower() == "attaquer":
        if classe_choisie == 0:
            niveau_de_sort = int(input("vous voulez lancer un sort de niveau combien ?: "))
            if Francois.get_mana() <= 0 or Francois.get_mana()-(niveau_de_sort * 20)<0: 
                print("Vous n'avez pas assez de mana pour attaquer")
                
                
            else : 
                Michel.magic_dammage_reduction(Francois.weapon.magic_damage, niveau_de_sort, Francois)
                print(Francois.get_mana())
        if classe_choisie ==  1:
            Michel.dammage_reduction(Francois.weapon.dammage, Francois)
            
                
        
        print(f"François {Francois.hp_basic}")
        print(f"Michel {Michel.hp_basic}")
    
        


# print(Mage.name_classe) 

print(Michel.dammage_reduction(Francois.weapon.dammage))

# Michel.weapon.degats(Francois)
# print(Michel.weapon.degats(Francois))
# print(Francois.hp_basic)

#todo mettre en place les combats avec une interface qui marche 
#todo mettre en place différent niveau de difficulté
#todo faire des armes avec plus de crit mais moins de degats et inversemment 
#! regler la puissance des attaque des sorcier car trop pt et mettre un lvl de sort max
#! protection magique




