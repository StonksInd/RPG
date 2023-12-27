from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from enemys.enemy import Enemy
from random import randint

#armes physique
La_main = Weapons("Ta main", 10, 0, 0, 0)
Massue = Weapons("Une massue", 20, 0, 0, 20)#BONK
Lance = Weapons("lance", 50, 0, 0, 0)
Hache = Weapons("Hache", 30, 0, 0, 10)#ce n'est pas moi madame c'est la hache

#armes magiques
Baton = Weapons("un baton", 20, 10, 0, 10)
Baguette = Weapons("baguette", 0, 30, 50, 0)#la france
Sceptre = Weapons("Sceptre", 20, 20, 100, 0)


#armures physique
pas_armure = Armor("pas d'armure", 0, 0, 0)
armure_legere = Armor("armure legere", 30, 0, 50)
armure_moyenne = Armor("armure moyenne", 75, 10, 20)
armure_lourde = Armor("armure lourde", 130, 15, 0)#le PEKKA

#armures magiques
armure_magique = Armor("armure magique", 20, 0, 100)#c'est de la MAAAAGIIEEE
armure_full_parade = Armor("armure de renvoie de dégats", 0, 75, 0)#apres la pique je touche
armure_archmage = Armor("armure magique", 0, 0, 150)
    
       
#instance des enemies physique
Gobelin = Enemy("Gobelin", 50, armure_legere, weapon_hivemind)
Hobogoblin = Enemy("Hobogoblin", 150, armure_moyenne, weapon_hivemind)
Orc = Enemy("Orc", 250, armure_lourde, weapon_hivemind)
Ogre = Enemy("Ogre", 350, pas_armure, weapon_hivemind)

#instance des enemies magique
Salamendre_elementaire = Enemy("Salamendre de feu", 100, armor_thornmail, weapon_hivemind)
Sorciere = Enemy("Sorciere", 100, armor_thornmail, weapon_hivemind)
Golem_magique = Enemy("Golem magique", 100, armor_thornmail, weapon_hivemind)
Elentaire = Enemy("Esprit élémentaire", 100, armor_thornmail, weapon_hivemind)


classe = [Mage, Barbarian]
armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
weapon = [La_main, Massue, Lance, Hache, Baton, Baguette, Sceptre]
enemy = [Gobelin, Hobogoblin, Orc, Ogre, Salamendre_elementaire, Sorciere, Golem_magique, Elentaire]
classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)

Michel = Enemy("Enemy", 100, armure_moyenne, weapon_hivemind)
Francois = Mage("jean", armure_moyenne, weapon_riftmaker)

# name_user = str(input("quel est votre nom ? : "))
while classe_choisie < 0 or classe_choisie > len(classe)-1:
    classe_choisie = int(input("veuillez entrer votre classe, 0: Mage, 1: Barbarian "))
# while armor_choisie <0 or armor_choisie > len(armor)-1:
#     armor_choisie = int(input("quelle armure voulez vous 0:pas_armure, 1:armure_lourde 2:armor_thornmail "))
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

#print(Michel.dammage_reduction(Francois.weapon.dammage))

# Michel.weapon.degats(Francois)
# print(Michel.weapon.degats(Francois))
# print(Francois.hp_basic)

#todo mettre en place les combats avec une interface qui marche 
#todo mettre en place différent niveau de difficulté
#todo faire des armes avec plus de crit mais moins de degats et inversemment 
#! regler la puissance des attaque des sorcier et mettre un lvl de sort max
#! instancier les 2 attaques pour le barbare




