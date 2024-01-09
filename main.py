from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from enemys.enemy import Enemy
from random import randint
from gears.spell import Spell

#armes physique
La_main = Weapons("Ta main", 10, 0, 0, 0)
Massue = Weapons("Une massue", 20, 0, 0, 40)#BONK
Lance = Weapons("lance", 50, 0, 0, 0, 20)
Hache = Weapons("Hache", 30, 0, 0, 20, 15)#ce n'est pas moi madame c'est la hache

#armes magiques
Baton = Weapons("un baton", 20, 1, 0, 10)
Baguette = Weapons("baguette", 0, 3, 50, 0)#la france
Sceptre = Weapons("Sceptre", 20, 2, 100, 0)


#armures physique
pas_armure = Armor("pas d'armure", 0, 0, 0)
armure_legere = Armor("armure legere", 30, 0, 50)
armure_moyenne = Armor("armure moyenne", 75, 10, 20)
armure_lourde = Armor("armure lourde", 130, 15, 0)#le PEKKA

#armures magiques
armure_magique = Armor("armure magique", 20, 0, 100)#c'est de la MAAAAGIIEEE
armure_full_parade = Armor("armure de renvoie de dégats", 0, 75, 0)#apres la pique je touche
armure_archmage = Armor("armure d'archmage", 0, 0, 150)
    
       
#instance des enemies physique
Gobelin = Enemy("Gobelin", 50, armure_legere, Massue, "physique")
Hobogoblin = Enemy("Hobogoblin", 150, armure_moyenne, Lance, "physique")
Orc = Enemy("Orc", 250, armure_lourde, Hache, "physique")
Ogre = Enemy("Ogre", 350, pas_armure, Massue, "physique")

#instance des enemies magique
Salamendre_elementaire = Enemy("Salamendre de feu", 100, armure_full_parade, La_main, "magique")
Sorciere = Enemy("Sorciere", 150, armure_archmage, Baguette, "magique")
Golem_magique = Enemy("Golem magique", 450, armure_lourde, La_main, "magique")
Elentaire = Enemy("Esprit élémentaire", 200, armure_archmage, Sceptre, "magique")

#instance des sorts
Etincelle = Spell("ettincelle", 10, 45)
Boule_de_feu = Spell("boule de feu", 20, 60)
Vague_tonante = Spell("vague tonante", 50, 100)

classe = [Mage, Barbarian]
armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
weapon = [La_main, Massue, Lance, Hache, Baton, Baguette, Sceptre]
spell = [Etincelle,Boule_de_feu, Vague_tonante]
enemie_physique= [Gobelin, Hobogoblin, Orc, Ogre]
enemie_magique =[Salamendre_elementaire, Sorciere, Golem_magique, Elentaire]
classe_choisie, armor_choisie, weapon_choisie, difficulte_choisie = len(classe), len(armor), len(weapon), len(enemie_physique)

def send_name(tab):
    str_return = ""
    for i in range (len(tab)):
        str_return += str(i) + ":" + str(tab[i])+ ", "
    return str_return



name_user = str(input("quel est votre nom ? : "))
while classe_choisie < 0 or classe_choisie > len(classe)-1:
    classe_choisie = int(input(f"veuillez entrer votre classe 0:Mage, 1:Barbarian "))
while armor_choisie <0 or armor_choisie > len(armor)-1:
    armor_choisie = int(input(f"quelle armure voulez vous {send_name(armor)} "))
while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
    weapon_choisie = int(input(f"quelle arme voulez vous {send_name(weapon)} "))
while difficulte_choisie < 0 or difficulte_choisie > len(enemie_magique)-1:
    difficulte_choisie = int(input("quelle difficulté voulez vous ? la 1, 2, 3 ou 4 ")) -1

enemie = [enemie_physique[difficulte_choisie],enemie_magique[difficulte_choisie]]
User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])

print("--------------------------------------")
print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
print(f"Vous avez choisi {User_1.name_classe} comme classe, elle à {User_1.hp_basic} point de vie")
print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} d'armure, {User_1.armor.magic_resistance} d'armure magique et {User_1.armor.thorns} de thorns. ")
print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégats, {User_1.weapon.magic_damage} dégat magique, donne {User_1.weapon.mana} mana et donne {User_1.weapon.armor_weapon} points d'armures.")



            
            

#! mettre en place arena avec un clean du main en cours



#! Classe arena 

#? Bonus
#?Carte et salle 
#? pouvoir utiliser 2 personnage en mode campagne (en multi quoi)
