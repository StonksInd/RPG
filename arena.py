

class Arena:
    
    def __init__(self,
                 User_1,
                 User_2,
                 ):
        self.User_1 = User_1
        self.User_2 = User_2
        
        
    def fight(self, User_1, User_2):
        users = [User_1, User_2]
        while True:
            if User_1.hp_basic<=0:
                print(f"{User_1.name_perso} est mort, {User_2.name_perso} a gagné !")
                break
            
            if User_2.hp_basic<=0:
                print(f"{User_2.name_perso} est mort, {User_1.name_perso} a gagné !")
                break            

            print(f"User 1 a {User_1.hp_basic} point de vie")
            print(f"User 2 a {User_2.hp_basic} point de vie")
            
            for i in range (len(users)):
                if classe_choisie == 0:
                    input_user = str(input(f"quel est votre action {users[i]} ? vous reposer ou attaquer ? "))
                    
                    if input_user.lower() == "attaquer":
                        input_user = str(input("vous voulez lancer un sort ou taper au corps à corps ? "))
                        
                        if input_user.lower() == "lancer":
                            sort_a_lancer = int(input(f"vous voulez lancer quel sort {print(send_name(spell))} ? ")) 
                                                
                            if users[i].get_mana() <= 0 or users[i].get_mana()-(spell[sort_a_lancer].mana_cost)<0:
                                print("Vous n'avez pas assez de mana pour attaquer")
                                print("--------------------------------------")
                            
                            else : 
                                users[i-1].magic_dammage_reduction(users[i].weapon.magic_damage, spell[sort_a_lancer], users[i])
                                print(f"vous avez {users[i].get_mana()} mana")
                                print("--------------------------------------")
                                
                        if input_user.lower() == "taper":
                            users[i-1].dammage_reduction(users[i].weapon.dammage, users[i])
                            print(f"vous attaquez {users[i-1].name_perso}")
                            print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print(f"vousrecupérez {users[i].recup_mana()} mana")
                        print(f"vous avez {users[i].get_mana()} mana")
                        print("--------------------------------------")
                        
                        
                if classe_choisie ==  1:
                    for i in range(2):
                        input_user = str(input("quel est votre action ? vous reposer ou attaquer ? "))
                    
                    if input_user.lower() == "attaquer":
                        users[i-1].dammage_reduction(users[i].weapon.dammage, users[i])
                        print(f"vous attaquez {enemie[nb_enemie].name_perso}")
                        print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print(f"vous recupérez {users[i].recup_hp()} hp")
                        print(f"vous avez {users[i].hp_basic()} hp")
                        print("--------------------------------------")
    
    def adventure(self, User_1):
        nb_enemie = 0
    while True:
        if User_1.hp_basic<=0:
            print("vous êtes mort dommage")
            break
        if nb_enemie >= len(enemie):
            print("vous avez vaincu tout les enemies")
            break
        if enemie[nb_enemie].hp_basic<=0:
            print(f"vous avez vaincu un(e) {enemie[nb_enemie].name_perso}")
            nb_enemie+=1
            

            
        else:
            print("--------------------------------------")
            print(f"vous avez {User_1.hp_basic} point de vie")
            print(f"{enemie[nb_enemie].name_perso} à {enemie[nb_enemie].hp_basic} point de vie")
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
                            print(f"{User_1.name_perso} utilise {spell[sort_a_lancer].spell_name} sur {enemie[nb_enemie].name_perso}, {User_1.name_perso} a {User_1.get_mana()} mana")
                            enemie[nb_enemie].magic_dammage_reduction(User_1.weapon.magic_damage, spell[sort_a_lancer], User_1)
                            print("--------------------------------------")
                            
                    if input_user.lower() == "taper":
                        print(f"{User_1.name_perso} attaque {enemie[nb_enemie].name_perso} avec {User_1.weapon.name_weapon}")
                        enemie[nb_enemie].dammage_reduction(User_1.weapon.dammage, User_1)
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
                        print(f"{User_1.name_perso} attaque {enemie[nb_enemie].name_perso} avec {User_1.weapon.name_weapon}")
                        enemie[nb_enemie].dammage_reduction(User_1.weapon.dammage, User_1)
                        print("--------------------------------------")

                            
                    if input_user.lower() == "reposer":
                        print(f"vous recupérez {abs(User_1.recup_hp()-User_1.hp_basic())} hp")
                        print(f"vous avez {User_1.hp_basic()} hp")
                        print("--------------------------------------")

            if enemie[nb_enemie].return_type() == "physique":
                enemie_attack = randint(0,6)
                if enemie_attack <=3:
                    print(f"{enemie[nb_enemie].name_perso} attaque {User_1.name_perso} avec {enemie[nb_enemie].weapon.name_weapon}")
                    User_1.dammage_reduction(enemie[nb_enemie].weapon.dammage, enemie[nb_enemie])
                    
                if enemie_attack >= 4:
                    print(f"{enemie[nb_enemie].name_perso} recupère {abs(enemie[nb_enemie].hp_basic -enemie[nb_enemie].recup_hp())} hp")
                    print(f"{enemie[nb_enemie].name_perso} a {enemie[nb_enemie].hp_basic} hp")
                    print("--------------------------------------")

            if enemie[nb_enemie].return_type() == "magique":
                enemie_attack <= randint(0,7)
                if enemie_attack <=3:
                    sort_lance = spell[randint(0, len(spell))]
                    if enemie[nb_enemie].get_mana() <= 0 or enemie[nb_enemie].get_mana()-(sort_lance.mana_cost)<0:
                        print(f"{enemie[nb_enemie].name_perso} recupère {abs(enemie[enemie[nb_enemie].get_mana()-nb_enemie].recup_mana())} mana")
                        print(f"{enemie[nb_enemie].name_perso} a {enemie[nb_enemie].get_mana()} mana")
                        print("--------------------------------------")

                    else : 
                        User_1.magic_dammage_reduction(enemie[nb_enemie].weapon.magic_damage, spell, enemie[nb_enemie])
                        print(f"{enemie[nb_enemie].name_perso} utilise {spell.spell_name}, il lui reste {enemie[nb_enemie].get_mana()} mana")
                        print("--------------------------------------")

                if enemie_attack == 4:
                    print(f"{enemie[nb_enemie].name_perso} recupère {abs(enemie[enemie[nb_enemie].get_mana()-nb_enemie].recup_mana())} mana")
                    print(f"{enemie[nb_enemie].name_perso} a {enemie[nb_enemie].get_mana()} mana")
                    print("--------------------------------------")

                else:
                    print(f"{enemie[nb_enemie].name_perso} attaque {User_1.name_perso} avec {enemie[nb_enemie].weapon.name_weapon}")
                    User_1.dammage_reduction(enemie[nb_enemie].weapon.dammage, enemie[nb_enemie])
                    print("--------------------------------------")

