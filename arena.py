

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
        pass