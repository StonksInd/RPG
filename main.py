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
Gobelin = Enemy("Gobelin", 50, armure_legere, Massue)
Hobogoblin = Enemy("Hobogoblin", 150, armure_moyenne, Lance)
Orc = Enemy("Orc", 250, armure_lourde, Hache)
Ogre = Enemy("Ogre", 350, pas_armure, Massue)

#instance des enemies magique
Salamendre_elementaire = Enemy("Salamendre de feu", 100, armure_full_parade, La_main)
Sorciere = Enemy("Sorciere", 150, armure_archmage, Baguette)
Golem_magique = Enemy("Golem magique", 450, armure_lourde, La_main)
Elentaire = Enemy("Esprit élémentaire", 200, armure_archmage, Sceptre)

#instance des sorts
Etincelle = Spell("ettincelle", 10, 15)
Boule_de_feu = Spell("boule de feu", 20, 30)
Vague_tonante = Spell("vague tonante", 50, 70)

classe = [Mage, Barbarian]
armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
weapon = [La_main, Massue, Lance, Hache, Baton, Baguette, Sceptre]
enemie_physique= [Gobelin, Hobogoblin, Orc, Ogre]
enemie_magique =[Salamendre_elementaire, Sorciere, Golem_magique, Elentaire]
classe_choisie, armor_choisie, weapon_choisie, difficulte_choisie = len(classe), len(armor), len(weapon), len(enemie_physique)

# Michel = Enemy("Enemy", 100, armure_moyenne, Baton)
# Francois = Mage("jean", armure_moyenne, Baton)

name_user = str(input("quel est votre nom ? : "))
while classe_choisie < 0 or classe_choisie > len(classe)-1:
    classe_choisie = int(input("veuillez entrer votre classe, 0: Mage, 1: Barbarian "))
while armor_choisie <0 or armor_choisie > len(armor)-1:
    armor_choisie = int(input("quelle armure voulez vous 0:pas_armure, 1:armure_legere, 2:armure_moyenne, 3:armure_lourde, 4:armure_magique, 5:armure_full_parade, 6:armure_archmage "))
while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
    weapon_choisie = int(input("quelle arme voulez vous 0:La_main, 1:Massue, 2:Lance, 3:Hache, 4:Baton, 5:Baguette, 6:Sceptre "))
while difficulte_choisie < 0 or difficulte_choisie > len(enemie_magique)-1:
    difficulte_choisie = int(input("quelle difficulté voulez vous ? la 1, 2, 3 ou 4 ")) -1

enemie = [enemie_physique[difficulte_choisie],enemie_magique[difficulte_choisie]]
User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])

print("--------------------------------------")
print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
print(f"Vous avez choisi {User_1.name_classe} comme classe, elle à {User_1.hp_basic} point de vie")
print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} d'armure, {User_1.armor.magic_resistance} d'armure magique et {User_1.armor.thorns} de thorns. ")
print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégats, {User_1.weapon.magic_damage} dégat magique, donne {User_1.weapon.mana} mana et donne {User_1.weapon.armor_weapon} points d'armures.")
print("--------------------------------------")

nb_enemie = 0
while True:
    if User_1.hp_basic<=0:
        print("vous êtes mort dommage")
        break
    if nb_enemie >= len(enemie):
        print("vous avez vaincu tout les enemies")
        break
    if enemie[nb_enemie].hp_basic<=0:
        print(f"vous avez vaincu un {enemie[nb_enemie].name_perso}")
        nb_enemie+=1
        

        
    else:
        #input_user = str(input("veuillez entrer votre action : "))
        # if input_user.lower() == "quitter":
        #     print("vous quitez le jeu")
        #     break
        
        print(f"vous avez {User_1.hp_basic} point de vie")
        print(f"{enemie[nb_enemie].name_perso} à {enemie[nb_enemie].hp_basic} point de vie")
        if classe_choisie == 0:
            input_user = str(input("quel est votre action ? vous reposer ou attaquer ? "))
            
            if input_user.lower() == "attaquer":
                niveau_de_sort = int(input("vous voulez lancer un sort de niveau combien ?: "))
                
                if User_1.get_mana() <= 0 or User_1.get_mana()-(niveau_de_sort * 20)<0: 
                    print("Vous n'avez pas assez de mana pour attaquer")
                    print("--------------------------------------")
                
                else : 
                    enemie[nb_enemie].magic_dammage_reduction(User_1.weapon.magic_damage, niveau_de_sort, User_1)
                    print(f"vous avez {User_1.get_mana()} mana")
                    print("--------------------------------------")
            
                    
            if input_user.lower() == "reposer":
                print(f"vousrecupérez {User_1.recup_mana()} mana")
                print(f"vous avez {User_1.get_mana()} mana")
                print("--------------------------------------")
                
             
        if classe_choisie ==  1:
            enemie[nb_enemie].dammage_reduction(User_1.weapon.dammage, User_1)
        
            
            
                
        

    
        


# print(Mage.name_classe) 

#print(Michel.dammage_reduction(Francois.weapon.dammage))

# Michel.weapon.degats(Francois)
# print(Michel.weapon.degats(Francois))
# print(Francois.hp_basic)



#todo faire des armes avec plus de crit mais moins de degats et inversemment 
#! regler la puissance des attaque des sorcier  et ajouter des sort 
#! instancier les 2 attaques pour le barbare et tout basiquement
#! faire les attaques en mode machin attaque machin avec telle arme


#! donner le choix au magicien entre lancer un sort ou attaquer avec son arme en choissisant sont sort
#! Classe arena 

#? Bonus
#?Carte et salle 
#? pouvoir utiliser 2 personnage en mode campagne (en multi quoi)
