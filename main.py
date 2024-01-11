from arena import Arena

input_us = ""
while input_us.lower() !="fight" and input_us.lower() != "adventure":
    input_us = input("quel mode voulez vous jouer ? : FIGHT (un 1vs1) / ADVENTURE (le mode histoire) ")
if input_us.lower() == "fight":
    Arena.fight()
       
if input_us.lower() == "adventure":
    Arena.adventure()