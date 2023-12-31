from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from enemys.enemy import Ennemi
from random import randint
from gears.spell import Spell

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
    
       
#instance des ennemies physique
Gobelin = Ennemi("Gobelin", 50, armure_legere, Massue, "physique")
Hobogoblin = Ennemi("Hobogoblin", 150, armure_moyenne, Lance, "physique")
Orc = Ennemi("Orc", 250, armure_lourde, Hache, "physique")
Ogre = Ennemi("Ogre", 350, pas_armure, Massue, "physique")

#instance des ennemies magique
Salamendre_elementaire = Ennemi("Salamendre de feu", 100, armure_full_parade, La_main, "magique")
Sorciere = Ennemi("Sorciere", 150, armure_archmage, Baguette, "magique")
Golem_magique = Ennemi("Golem magique", 450, armure_lourde, La_main, "magique")
Elentaire = Ennemi("Esprit élémentaire", 200, armure_archmage, Sceptre, "magique")

#instance des sorts
Etincelle = Spell("ettincelle", 10, 45)
Boule_de_feu = Spell("boule de feu", 20, 60)
Vague_tonante = Spell("vague tonante", 50, 100)

class Arena:
    
    @staticmethod 
    def fight():
        classe = [Mage, Barbarian]
        armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
        weapon = [La_main, Massue, Lance, Hache, Baton, Baguette, Sceptre]
        spell = [Etincelle,Boule_de_feu, Vague_tonante]
        ennemie_physique= [Gobelin, Hobogoblin, Orc, Ogre]
        ennemie_magique =[Salamendre_elementaire, Sorciere, Golem_magique, Elentaire]
        classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)

        def send_name(tab):
            str_return = ""
            for i in range (len(tab)):
                str_return += str(i) + ":" + str(tab[i])+ ", "
            return str_return
        
        name_user = str(input("quel est votre nom ? Utilisateur 1 : "))
        while classe_choisie < 0 or classe_choisie > len(classe)-1:
            classe_choisie = int(input(f"veuillez entrer votre classe 0:Mage, 1:Barbarian "))
        while armor_choisie <0 or armor_choisie > len(armor)-1:
            armor_choisie = int(input(f"quelle armure voulez vous {send_name(armor)} "))
        while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
            weapon_choisie = int(input(f"quelle arme voulez vous {send_name(weapon)} "))
        
        User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])
        classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)
        
        name_user = str(input("quel est votre nom ? Utilisateur 2 : "))
        while classe_choisie < 0 or classe_choisie > len(classe)-1:
            classe_choisie = int(input(f"veuillez entrer votre classe 0:Mage, 1:Barbarian "))
        while armor_choisie <0 or armor_choisie > len(armor)-1:
            armor_choisie = int(input(f"quelle armure voulez vous {send_name(armor)} "))
        while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
            weapon_choisie = int(input(f"quelle arme voulez vous {send_name(weapon)} "))
        
        User_2 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])
        
        
        while True:
            users = [User_1, User_2]
            if User_1.hp_basic<=0:
                print(f"{User_1.name_perso} est mort, {User_2.name_perso} a gagné !")
                break
            
            if User_2.hp_basic<=0:
                print(f"{User_2.name_perso} est mort, {User_1.name_perso} a gagné !")
                break            

            print(f"{User_1.name_perso} a {User_1.hp_basic} point de vie")
            print(f"{User_2.name_perso} a {User_2.hp_basic} point de vie")
            
            for i in range (0, len(users)):
                if users[i].name_classe == "mage":
                    input_user = str(input(f"quel est votre action {users[i].name_perso} ? vous reposer ou attaquer ? "))
                    
                    if input_user.lower() == "attaquer":
                        input_user = str(input("vous voulez lancer un sort ou taper au corps à corps ? "))
                        
                        if input_user.lower() == "lancer":
                            sort_a_lancer = int(input(f"vous voulez lancer quel sort {send_name(spell)} ? ")) 
                                                
                            if users[i].get_mana() <= 0 or users[i].get_mana()-(spell[sort_a_lancer].mana_cost)<0:
                                print("Vous n'avez pas assez de mana pour attaquer")
                                print("--------------------------------------")
                            
                            else : 
                                users[i-1].magic_dammage_reduction(users[i].weapon.magic_damage, spell[sort_a_lancer], users[i])
                                print(f"{users[i].name_perso} a {users[i].get_mana()} mana")
                                print("--------------------------------------")
                                
                        if input_user.lower() == "taper":
                            users[i-1].dammage_reduction(users[i].weapon.dammage, users[i])
                            print(f"vous attaquez {users[i-1].name_perso}")
                            print("--------------------------------------")

                            
                        if input_user.lower() == "reposer":
                            print(f"vousrecupérez {users[i].recup_mana()} mana")
                            print(f"vous avez {users[i].get_mana()} mana")
                            print("--------------------------------------")
                    i+=1
                        
                        
                if users[i].name_classe ==  "Barbarian":
                    for i in range(2):
                        input_user = str(input(f"quel est votre action {users[i].name_perso}? vous reposer ou attaquer ? "))
                    
                    if input_user.lower() == "attaquer":
                        users[i-1].dammage_reduction(users[i].weapon.dammage, users[i])
                        print(f"vous attaquez {users[i-1].name_perso}")
                        print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print(f"vous recupérez {users[i].recup_hp()} hp")
                        print(f"vous avez {users[i].hp_basic()} hp")
                        print("--------------------------------------")
                    i+=1
    
    def adventure():
        classe = [Mage, Barbarian]
        armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
        weapon = [La_main, Massue, Lance, Hache, Baton, Baguette, Sceptre]
        spell = [Etincelle,Boule_de_feu, Vague_tonante]
        ennemie_physique= [Gobelin, Hobogoblin, Orc, Ogre]
        ennemie_magique =[Salamendre_elementaire, Sorciere, Golem_magique, Elentaire]
        classe_choisie, armor_choisie, weapon_choisie, difficulte_choisie = len(classe), len(armor), len(weapon), len(ennemie_physique)

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
        while difficulte_choisie < 0 or difficulte_choisie > len(ennemie_magique)-1:
            difficulte_choisie = int(input("quelle difficulté voulez vous ? la 1, 2, 3 ou 4 ")) -1

        ennemie = [ennemie_physique[difficulte_choisie],ennemie_magique[difficulte_choisie]]
        User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])

        print("--------------------------------------")
        print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
        print(f"Vous avez choisi {User_1.name_classe} comme classe, elle à {User_1.hp_basic} point de vie")
        print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} d'armure, {User_1.armor.magic_resistance} d'armure magique et {User_1.armor.thorns} de thorns. ")
        print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégats, {User_1.weapon.magic_damage} dégat magique, donne {User_1.weapon.mana} mana et donne {User_1.weapon.armor_weapon} points d'armures.")

        nb_ennemie = 0
        while True:
            if User_1.hp_basic<=0:
                print("vous êtes mort dommage")
                break
            if nb_ennemie >= len(ennemie):
                print("vous avez vaincu tout les ennemies")
                break
            if ennemie[nb_ennemie].hp_basic<=0:
                print(f"vous avez vaincu un(e) {ennemie[nb_ennemie].name_perso}")
                nb_ennemie+=1
                
  
            else:
                print("--------------------------------------")
                print(f"vous avez {User_1.hp_basic} point de vie")
                print(f"{ennemie[nb_ennemie].name_perso} à {ennemie[nb_ennemie].hp_basic} point de vie")
                if classe_choisie == 0:
                    input_user = str(input("quel est votre action ? vous reposer ou attaquer ? "))
                    
                    if input_user.lower() == "attaquer":
                        input_user = str(input("vous voulez lancer un sort ou taper au corps à corps ? "))
                        
                        
                        if input_user.lower() == "lancer":
                            sort_a_lancer = int(input(f"vous voulez lancer quel sort {send_name(spell)} ? ")) 
                            print("--------------------------------------")
                            if User_1.get_mana() <= 0 or User_1.get_mana()-(spell[sort_a_lancer].mana_cost)<0:
                                print("Vous n'avez pas assez de mana pour attaquer")
                                print("--------------------------------------")
                            
                            else : 
                                print(f"{User_1.name_perso} utilise {spell[sort_a_lancer].spell_name} sur {ennemie[nb_ennemie].name_perso}, {User_1.name_perso} a {User_1.get_mana()} mana")
                                ennemie[nb_ennemie].magic_dammage_reduction(User_1.weapon.magic_damage, spell[sort_a_lancer], User_1)
                                print("--------------------------------------")
                                
                        if input_user.lower() == "taper":
                            print(f"{User_1.name_perso} attaque {ennemie[nb_ennemie].name_perso} avec {User_1.weapon.name_weapon}")
                            ennemie[nb_ennemie].dammage_reduction(User_1.weapon.dammage, User_1)
                            print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print("--------------------------------------")
                        print(f"vousrecupérez {abs(User_1.mana_basic-User_1.recup_mana())} mana") #modifier pour avoir le mana en négatif
                        print(f"vous avez {User_1.get_mana()} mana")
                        print("--------------------------------------")
                        
                    
                if classe_choisie ==  1:
                    for i in range(2):
                        input_user = str(input("quel est votre action ? vous reposer ou attaquer ? "))
                        print("--------------------------------------")
                    
                        if input_user.lower() == "attaquer":
                            print(f"{User_1.name_perso} attaque {ennemie[nb_ennemie].name_perso} avec {User_1.weapon.name_weapon}")
                            ennemie[nb_ennemie].dammage_reduction(User_1.weapon.dammage, User_1)
                            print("--------------------------------------")

                                
                        if input_user.lower() == "reposer":
                            print(f"vous recupérez {abs(User_1.recup_hp()-User_1.hp_basic())} hp")
                            print(f"vous avez {User_1.hp_basic()} hp")
                            print("--------------------------------------")

                if ennemie[nb_ennemie].return_type() == "physique":
                    ennemie_attack = randint(0,6)
                    if ennemie_attack <=3:
                        print(f"{ennemie[nb_ennemie].name_perso} attaque {User_1.name_perso} avec {ennemie[nb_ennemie].weapon.name_weapon}")
                        User_1.dammage_reduction(ennemie[nb_ennemie].weapon.dammage, ennemie[nb_ennemie])
                        
                    if ennemie_attack >= 4:
                        print(f"{ennemie[nb_ennemie].name_perso} recupère {abs(ennemie[nb_ennemie].hp_basic -ennemie[nb_ennemie].recup_hp())} hp")
                        print(f"{ennemie[nb_ennemie].name_perso} a {ennemie[nb_ennemie].hp_basic} hp")
                        print("--------------------------------------")

                if ennemie[nb_ennemie].return_type() == "magique":
                    ennemie_attack <= randint(0,7)
                    if ennemie_attack <=3:
                        sort_lance = spell[randint(0, len(spell))]
                        if ennemie[nb_ennemie].get_mana() <= 0 or ennemie[nb_ennemie].get_mana()-(sort_lance.mana_cost)<0:
                            print(f"{ennemie[nb_ennemie].name_perso} recupère {abs(ennemie[ennemie[nb_ennemie].get_mana()-nb_ennemie].recup_mana())} mana")
                            print(f"{ennemie[nb_ennemie].name_perso} a {ennemie[nb_ennemie].get_mana()} mana")
                            print("--------------------------------------")

                        else : 
                            User_1.magic_dammage_reduction(ennemie[nb_ennemie].weapon.magic_damage, spell, ennemie[nb_ennemie])
                            print(f"{ennemie[nb_ennemie].name_perso} utilise {spell.spell_name}, il lui reste {ennemie[nb_ennemie].get_mana()} mana")
                            print("--------------------------------------")

                    if ennemie_attack == 4:
                        print(f"{ennemie[nb_ennemie].name_perso} recupère {abs(ennemie[ennemie[nb_ennemie].get_mana()-nb_ennemie].recup_mana())} mana")
                        print(f"{ennemie[nb_ennemie].name_perso} a {ennemie[nb_ennemie].get_mana()} mana")
                        print("--------------------------------------")

                    else:
                        print(f"{ennemie[nb_ennemie].name_perso} attaque {User_1.name_perso} avec {ennemie[nb_ennemie].weapon.name_weapon}")
                        User_1.dammage_reduction(ennemie[nb_ennemie].weapon.dammage, ennemie[nb_ennemie])
                        print("--------------------------------------")

