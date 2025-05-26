from arena import Arena

input_us = -1
while input_us != 0 and input_us != 1:
    input_us = int(input("À quel mode voulez-vous jouer ? : 0 Combat (1vs1) / 1 mode histoire : "))
if input_us == 0:
    Arena.fight()
       
if input_us == 1:
    Arena.adventure()