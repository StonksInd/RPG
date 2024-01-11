from characters.character import Character
from characters.barbarian import Barbarian
from characters.mage import Mage
from gears.armor import Armor
from gears.weapon import Weapons
from ennemis.ennemi import Ennemi
from random import randint
from gears.spell import Spell

#armes physique
la_main = Weapons(" À la main", 10, 0, 0, 0)
massue = Weapons(" Une massue", 20, 0, 0, 40)#BONK
lance = Weapons(" Lance", 50, 0, 0, 0, 20)
hache = Weapons(" Hache", 30, 0, 0, 20, 15)#ce n'est pas moi madame c'est la hache

#armes magiques
baton = Weapons(" Un bâton", 20, 1, 0, 10)
baguette = Weapons(" Baguette", 0, 3, 50, 0)#la france
sceptre = Weapons(" Sceptre", 20, 2, 100, 0)


#armures physique
pas_armure = Armor(" Aucune armure", 0, 0, 0)
armure_legere = Armor(" Armure légère", 30, 0, 50)
armure_moyenne = Armor(" Armure moyenne", 75, 10, 20)
armure_lourde = Armor(" Armure lourde", 130, 15, 0)#le PEKKA

#armures magiques
armure_magique = Armor(" Armure magique", 20, 0, 100)#c'est de la MAAAAGIIEEE
armure_full_parade = Armor(" Armure de renvoie de dégâts", 0, 75, 0)#apres la pique je touche
armure_archimage = Armor(" Armure d'archimage", 0, 0, 150)
    
       
#instance des ennemies physique
gobelin = Ennemi(" Gobelin", 50, armure_legere, massue, "physique")
hobogoblin = Ennemi(" Hobogoblin", 150, armure_moyenne, lance, "physique")
orc = Ennemi(" Orc", 250, armure_lourde, hache, "physique")
ogre = Ennemi(" Ogre", 350, pas_armure, massue, "physique")

#instance des ennemies magique
salamandre_elementaire = Ennemi(" Salamandre de feu", 100, armure_full_parade, la_main, "magique")
sorciere = Ennemi(" Sorcière", 150, armure_archimage, baguette, "magique")
golem_magique = Ennemi(" Golem magique", 450, armure_lourde, la_main, "magique")
elementaire = Ennemi(" Esprit élémentaire", 200, armure_archimage, sceptre, "magique")

#instance des sorts
etincelle = Spell(" Étincelle", 10, 45)
boule_de_feu = Spell(" Boule de feu", 20, 60)
vague_tonante = Spell(" Vague tonante", 50, 100)

class Arena:
    
    @staticmethod 
    def fight():
        classe = [Mage, Barbarian]
        armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archmage]
        weapon = [la_main, massue, lance, hache, baton, baguette, sceptre]
        spell = [etincelle, boule_de_feu, vague_tonante]
        ennemie_physique= [gobelin, hobogoblin, orc, ogre]
        ennemie_magique = [salamandre_elementaire, sorciere, golem_magique, elementaire]
        classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)

        def send_name(tab):
            str_return = ""
            for i in range (len(tab)):
                str_return += str(i) + ":" + str(tab[i])+ ", "
            return str_return
        
        name_user = str(input("Quel est votre nom ? Utilisateur 1 : "))
        while classe_choisie < 0 or classe_choisie > len(classe)-1:
            classe_choisie = int(input(f"Veuillez entrer votre classe 0: Mage, 1: Barbarian "))
        while armor_choisie <0 or armor_choisie > len(armor)-1:
            armor_choisie = int(input(f"Quelle armure voulez-vous ? : {send_name(armor)} "))
        while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
            weapon_choisie = int(input(f"Quelle arme voulez-vous ? : {send_name(weapon)} "))
        
        User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])
        classe_choisie, armor_choisie, weapon_choisie = len(classe), len(armor), len(weapon)
        
        name_user = str(input("Quel est votre nom ? Utilisateur 2 : "))
        while classe_choisie < 0 or classe_choisie > len(classe)-1:
            classe_choisie = int(input(f"Veuillez entrer votre classe 0: Mage, 1: Barbarian "))
        while armor_choisie <0 or armor_choisie > len(armor)-1:
            armor_choisie = int(input(f"Quelle armure voulez-vous ? : {send_name(armor)} "))
        while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
            weapon_choisie = int(input(f"Quelle arme voulez-vous ? : {send_name(weapon)} "))
        
        User_2 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])
        print("--------------------------------------")
        
        while True:
            users = [User_1, User_2]
            if User_1.hp_basic<=0:
                print(f"{User_1.name_perso} est mort, {User_2.name_perso} a gagné, par conséquent {User_1.name_perso} est un loser !")
                break
            
            if User_2.hp_basic<=0:
                print(f"{User_2.name_perso} est mort, {User_1.name_perso} a gagné, par conséquent {User_2.name_perso} est un loser !")
                break            
            

            for i in range (2):
                print(f"{User_1.name_perso} a {User_1.hp_basic} points de vie")
                print(f"{User_2.name_perso} a {User_2.hp_basic} points de vie")
                print("--------------------------------------")
                if users[i].name_classe == "mage":
                    input_user = ""
                    while input_user.lower() != "reposer" and input_user.lower() != "attaquer":
                        input_user = str(input(f"Quelle est votre action {users[i].name_perso} ? Vous REPOSER ou bien ATTAQUER ? "))
                    
                    if input_user.lower() == "attaquer":
                        input_user = ""
                        while input_user.lower() != "lancer" and input_user.lower() != "taper":
                            input_user = str(input("Vous voulez LANCER un sort ou bien TAPER au corps à corps ? "))
                        
                        if input_user.lower() == "lancer":
                            sort_a_lancer = int(input(f"Quel sort voulez-vous lancer ? : {send_name(spell)} ")) 
                                                
                            if users[i].get_mana() <= 0 or users[i].get_mana()-(spell[sort_a_lancer].mana_cost)<0:
                                print("Vous n'avez pas assez de mana pour attaquer")
                                print("--------------------------------------")
                            
                            else : 
                                print(f"{users[i].name_perso} utilise {spell[sort_a_lancer].spell_name} sur {users[i-1].name_perso}, {User_1.name_perso} possède dorénavant {User_1.get_mana()} points de mana")
                                users[i-1].magic_dammage_reduction(users[i].weapon.magic_damage, spell[sort_a_lancer], users[i])
                                print("--------------------------------------")
                                
                        if input_user.lower() == "taper":
                            print(f"{users[i].name_perso} attaque {users[i-1].name_perso} avec {users[i].weapon.name_weapon}")
                            users[i-1].dammage_reduction(users[i].weapon.dammage, users[i])
                            print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print(f"Vous récupérez {users[i].recup_mana()} points de mana")
                        print(f"Vous avez {users[i].get_mana()} points de mana")
                        print("--------------------------------------")
                    
                        
                        
                if users[i].name_classe ==  "Barbarian":
                    for j in range(2):
                        input_user = ""
                        while input_user.lower() != "reposer" and input_user.lower() != "attaquer":
                            input_user = str(input(f"Quelle est votre action {users[i].name_perso} ? Vous REPOSER ou bien ATTAQUER ? "))
                        
                    
                        if input_user.lower() == "attaquer":
                            print(f"{users[i].name_perso} attaque {users[i-1].name_perso} avec {users[i].weapon.name_weapon}")
                            users[i-1].dammage_reduction(users[i].weapon.dammage, users[i])
                            print("--------------------------------------")

                                
                        if input_user.lower() == "reposer":
                            print(f"Vous recupérez {users[i].recup_hp()} points de vie")
                            print(f"vous possédez {users[i].hp_basic()} points de vie")
                            print("--------------------------------------")
                
    
    def adventure():
        classe = [Mage, Barbarian]
        armor = [pas_armure, armure_legere, armure_moyenne, armure_lourde, armure_magique, armure_full_parade, armure_archimage]
        weapon = [la_main, massue, lance, hache, baton, baguette, sceptre]
        spell = [etincelle, boule_de_feu, vague_tonante]
        ennemie_physique= [gobelin, hobogoblin, orc, ogre]
        ennemie_magique =[salamandre_elementaire, sorciere, golem_magique, elementaire]
        classe_choisie, armor_choisie, weapon_choisie, difficulte_choisie = len(classe), len(armor), len(weapon), len(ennemie_physique)

        def send_name(tab):
            str_return = ""
            for i in range (len(tab)):
                str_return += str(i) + ":" + str(tab[i])+ ", "
            return str_return

        name_user = str(input("Quel est votre nom ? : "))
        while classe_choisie < 0 or classe_choisie > len(classe)-1:
            classe_choisie = int(input(f"Veuillez entrer votre classe 0: Mage, 1: Barbarian "))
        while armor_choisie <0 or armor_choisie > len(armor)-1:
            armor_choisie = int(input(f"Quelle armure voulez-vous ? : {send_name(armor)} "))
        while weapon_choisie < 0 or weapon_choisie > len(weapon)-1:
            weapon_choisie = int(input(f"Quelle arme voulez-vous ? : {send_name(weapon)} "))
        while difficulte_choisie < 0 or difficulte_choisie > len(ennemie_magique)-1:
            difficulte_choisie = int(input("Quelle difficulté voulez-vous ? : Difficulté 1, 2, 3 ou 4 ?")) -1

        ennemie = [ennemie_physique[difficulte_choisie],ennemie_magique[difficulte_choisie]]
        User_1 = classe[classe_choisie](name_user, armor[armor_choisie], weapon[weapon_choisie])

        print("--------------------------------------")
        print(f"Vous avez choisi {User_1.name_perso} comme nom. ")
        print(f"Vous avez choisi {User_1.name_classe} comme classe, elle a {User_1.hp_basic} points de vie")
        print(f"Vous avez choisi l'armure {User_1.armor.name_armor}, elle a {User_1.armor.armor} point(s) d'armure, {User_1.armor.magic_resistance} point(s) d'armure magique et {User_1.armor.thorns} de thorns. ")
        print(f"Vous avez choisi l'arme {User_1.weapon.name_weapon}, elle fait {User_1.weapon.dammage} dégâts, {User_1.weapon.magic_damage} dégât(s) magique(s), donne {User_1.weapon.mana} point(s) de mana et donne {User_1.weapon.armor_weapon} point(s) d'armure.")

        nb_ennemie = 0
        while True:
            if User_1.hp_basic<=0:
                print("Vous êtes mort, dommage il fallait être meilleur !")
                break
            if nb_ennemie >= len(ennemie):
                print("Vous avez vaincu tous les ennemis. Félicitation vous avez été meilleur ! ")
                break
            if ennemie[nb_ennemie].hp_basic<=0:
                print(f"Vous avez vaincu un(e) {ennemie[nb_ennemie].name_perso}. Va falloir continuer comme ça pèpère")
                nb_ennemie+=1
                
  
            else:
                print("--------------------------------------")
                print(f"Vous avez {User_1.hp_basic} points de vie")
                print(f"{ennemie[nb_ennemie].name_perso} a {ennemie[nb_ennemie].hp_basic} points de vie")
                if classe_choisie == 0:
                    input_user = ""
                    while input_user.lower() != "reposer" and input_user.lower() != "attaquer":
                        input_user = str(input(f"Quelle est votre action {User_1.name_perso} ? Vous REPOSER ou bien ATTAQUER ? "))
                        
                    if input_user.lower() == "attaquer":
                        input_user = ""
                        while input_user.lower() != "lancer" and input_user.lower() != "taper":
                            input_user = str(input("Voulez-vous LANCER un sort ou bien TAPER au corps à corps ? "))
                        
                        if input_user.lower() == "lancer":
                            sort_a_lancer = int(input(f"Quel sort voulez-vous lancer ? : {send_name(spell)} ? ")) 
                            print("--------------------------------------")
                            if User_1.get_mana() <= 0 or User_1.get_mana()-(spell[sort_a_lancer].mana_cost)<0:
                                print("Vous n'avez pas assez de points de mana pour attaquer")
                                print("--------------------------------------")
                            
                            else : 
                                print(f"{User_1.name_perso} utilise {spell[sort_a_lancer].spell_name} sur {ennemie[nb_ennemie].name_perso}, {User_1.name_perso} possède dorénavant {User_1.get_mana()} points de mana")
                                ennemie[nb_ennemie].magic_dammage_reduction(User_1.weapon.magic_damage, spell[sort_a_lancer], User_1)
                                print("--------------------------------------")
                                
                        if input_user.lower() == "taper":
                            print(f"{User_1.name_perso} attaque {ennemie[nb_ennemie].name_perso} avec {User_1.weapon.name_weapon}")
                            ennemie[nb_ennemie].dammage_reduction(User_1.weapon.dammage, User_1)
                            print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print("--------------------------------------")
                        print(f"Vous recupérez {abs(User_1.mana_basic-User_1.recup_mana())} points de mana") #modifier pour avoir le mana en négatif
                        print(f"Vous possédez {User_1.get_mana()} points de mana")
                        print("--------------------------------------")
                        
                    
                if classe_choisie ==  1:
                    for i in range(2):
                        input_user = ""
                        while input_user.lower() != "reposer" and input_user.lower() != "attaquer":
                            input_user = str(input(f"Quelle est votre action {User_1.name_perso} ? Vous REPOSER ou bien ATTAQUER ? "))
                        print("--------------------------------------")
                    
                        if input_user.lower() == "attaquer":
                            print(f"{User_1.name_perso} attaque {ennemie[nb_ennemie].name_perso} avec {User_1.weapon.name_weapon}")
                            ennemie[nb_ennemie].dammage_reduction(User_1.weapon.dammage, User_1)
                            print("--------------------------------------")

                                
                        if input_user.lower() == "reposer":
                            print(f"Vous recupérez {abs(User_1.recup_hp()-User_1.hp_basic())} points de vie")
                            print(f"Vous avez {User_1.hp_basic()} points de vie")
                            print("--------------------------------------")

                if ennemie[nb_ennemie].return_type() == "physique":
                    ennemie_attack = randint(0,6)
                    if ennemie_attack <=3:
                        print(f"{ennemie[nb_ennemie].name_perso} attaque {User_1.name_perso} avec {ennemie[nb_ennemie].weapon.name_weapon}")
                        User_1.dammage_reduction(ennemie[nb_ennemie].weapon.dammage, ennemie[nb_ennemie])
                        
                    if ennemie_attack >= 4:
                        print(f"{ennemie[nb_ennemie].name_perso} se repose et recupère {abs(ennemie[nb_ennemie].hp_basic -ennemie[nb_ennemie].recup_hp())} points de vie")
                        print(f"{ennemie[nb_ennemie].name_perso} possède {ennemie[nb_ennemie].hp_basic} points de vie restants")
                        print("--------------------------------------")

                if ennemie[nb_ennemie].return_type() == "magique":
                    ennemie_attack <= randint(0,7)
                    if ennemie_attack <=3:
                        sort_lance = spell[randint(0, len(spell))]
                        if ennemie[nb_ennemie].get_mana() <= 0 or ennemie[nb_ennemie].get_mana()-(sort_lance.mana_cost)<0:
                            print(f"{ennemie[nb_ennemie].name_perso} se repose et recupère {abs(ennemie[ennemie[nb_ennemie].get_mana()-nb_ennemie].recup_mana())} points de mana")
                            print(f"{ennemie[nb_ennemie].name_perso} possède {ennemie[nb_ennemie].get_mana()} points de mana restants")
                            print("--------------------------------------")

                        else : 
                            User_1.magic_dammage_reduction(ennemie[nb_ennemie].weapon.magic_damage, spell, ennemie[nb_ennemie])
                            print(f"{ennemie[nb_ennemie].name_perso} utilise {spell.spell_name}, il lui reste {ennemie[nb_ennemie].get_mana()} points de mana")
                            print("--------------------------------------")

                    if ennemie_attack == 4:
                        print(f"{ennemie[nb_ennemie].name_perso} se repose et recupère {abs(ennemie[ennemie[nb_ennemie].get_mana()-nb_ennemie].recup_mana())} points de mana")
                        print(f"{ennemie[nb_ennemie].name_perso} possède {ennemie[nb_ennemie].get_mana()} points de mana restants")
                        print("--------------------------------------")

                    else:
                        print(f"{ennemie[nb_ennemie].name_perso} attaque {User_1.name_perso} avec {ennemie[nb_ennemie].weapon.name_weapon}")
                        User_1.dammage_reduction(ennemie[nb_ennemie].weapon.dammage, ennemie[nb_ennemie])
                        print("--------------------------------------")

