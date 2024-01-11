from arena import Arena

input_us = ""
while input_us.lower() !="fight" and input_us.lower() != "adventure":
    input_us = input("À quel mode voulez-vous jouer ? : FIGHT (1vs1) / ADVENTURE (mode histoire) :")
if input_us.lower() == "fight":
    Arena.fight()
       
if input_us.lower() == "adventure":
    Arena.adventure()