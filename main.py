from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from ennemis.ennemi import Ennemi
from random import randint
from gears.spell import Spell

#armes physique
la_main = Weapons(" Ta main", 10, 0, 0, 0)
massue = Weapons(" Une massue", 20, 0, 0, 40)#BONK
lance = Weapons(" Lance", 50, 0, 0, 0, 20)
hache = Weapons(" Hache", 30, 0, 0, 20, 15)#ce n'est pas moi madame c'est la hache

#armes magiques
baton = Weapons(" Un bâton", 20, 1, 0, 10)
baguette = Weapons(" Baguette", 0, 3, 50, 0)#la france
sceptre = Weapons(" Sceptre", 20, 2, 100, 0)


#armures physique
aucune_armure = Armor(" Aucune armure", 0, 0, 0)
armure_legere = Armor(" Armure légère", 30, 0, 50)
armure_moyenne = Armor(" Armure moyenne", 75, 10, 20)
armure_lourde = Armor(" Armure lourde", 130, 15, 0)#le PEKKA

#armures magiques
armure_magique = Armor(" Armure magique", 20, 0, 100)#c'est de la MAAAAGIIEEE
armure_full_parade = Armor(" Armure de renvoie de dégâts", 0, 75, 0)#apres la pique je touche
armure_archimage = Armor(" Armure d'archimage", 0, 0, 150)
    
       
#instance des ennemis physique
gobelin = Ennemi("Gobelin", 50, armure_legere, massue, "physique")
hobogoblin = Ennemi("Hobogoblin", 150, armure_moyenne, lance, "physique")
orc = Ennemi("Orc", 250, armure_lourde, hache, "physique")
ogre = Ennemi("Ogre", 350, aucune_armure, massue, "physique")

#instance des ennemis magique
salamandre_elementaire = Ennemi("Salamandre de feu", 100, armure_full_parade, la_main, "magique")
sorciere = Ennemi("Sorcière", 150, armure_archimage, baguette, "magique")
golem_magique = Ennemi("Golem magique", 450, armure_lourde, la_main, "magique")
elementaire = Ennemi("Esprit élémentaire", 200, armure_archimage, sceptre, "magique")

#instance des sorts
etincelle = Spell(" Étincelle", 10, 45)
boule_de_feu = Spell(" Boule de feu", 20, 60)
vague_tonante = Spell(" Vague tonante", 50, 100)

classe = [Mage, Barbarian]
armor = [aucune_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archimage]
weapon = [la_main, massue, lance, hache, baton, baguette, sceptre]
spell = [etincelle,boule_de_feu, vague_tonante]
ennemi_physique= [gobelin, hobogoblin, orc, ogre]
ennemi_magique =[salamandre_elementaire, sorciere, golem_magique, elementaire]
classe_choisie, armor_choisie, weapon_choisie, difficulte_choisie = len(classe), len(armor), len(weapon), len(ennemi_physique)

def send_name(tab):
    str_return = ""
    for i in range (len(tab)):
        str_return += str(i) + ":" + str(tab[i])+ ", "
    return str_return



name_user = str(input("Quelle est votre nom ? : "))
while classe_choisie < 0 or classe_choisie > len(classe)-1:
    classe_choisie = int(input(f"Veuillez entrer votre classe 0: Mage, 1: Barbarian "))
while armor_choisie <0 or armor_choisie > len(armor)-1:
    armor_choisie = int(input(f"Quelle armure voulez-vous ? : {send_name(armor)} "))
while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
    weapon_choisie = int(input(f"Quelle arme voulez-vous ? : {send_name(weapon)} "))
while difficulte_choisie < 0 or difficulte_choisie > len(ennemi_magique)-1:
    difficulte_choisie = int(input("Quelle difficulté voulez-vous ? : La 1, 2, 3 ou 4 ?")) -1

ennemi = [ennemi_physique[difficulte_choisie],ennemi_magique[difficulte_choisie]]
User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])

print("--------------------------------------")
print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
print(f"Vous avez choisi {User_1.name_classe} comme classe, elle possède {User_1.hp_basic} points de vie.")
print(f"Vous avez choisi l'armure{User_1.armor.name_armor}, elle possède {User_1.armor.armor} point(s) d'armure, {User_1.armor.magic_resistance} point(s) d'armure magique et {User_1.armor.thorns} de point(s) de thorns. ")
print(f"Vous avez choisi l'arme{User_1.weapon.name_weapon}, elle inflige {User_1.weapon.dammage} points de dégâts, {User_1.weapon.magic_damage} point(s) de dégât(s) magique(s), donne {User_1.weapon.mana} point(s) de mana et donne {User_1.weapon.armor_weapon} point(s) d'armure.")



            
            

#! mettre en place arena avec un clean du main en cours



#! Classe arena 

#? Bonus
#?Carte et salle 
#? pouvoir utiliser 2 personnage en mode campagne (en multi quoi)
