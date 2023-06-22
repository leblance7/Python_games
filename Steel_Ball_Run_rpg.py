#STEELBALLRUN_rpg
#To create a text based, stragety rpg game, that allows battles between charcters based
# on stats of a character build.
#6-15-2022 start
#A function that allows the placement of stats using 
stand_name = input("Enter the name of your stand: ")
stand_stats = {"power": 0, "speed": 0, "range": 0, "stamina": 0, "precision": 0,
               "potential": 0, "vitality": 0}
level = 5


#level_up() alters the local varaible level to be gloabal, print statement

def level_up():
    global level
    print("Please enter the the stat you would like to increase.")

#creating the for loop to determine which stats your points go into,
#resets loop with corrected number to distrubte points and reuturn the updted dictionary

    for x in range(level):
        skill = input("Choose from power, p, speed, s, range, r, stamina, st,\n" +
                  "precision, pr, potential, po, or vitality, v: ").lower()
        # Case statements
        print(skill)
        if skill in ["p", "power"]: 
            stand_stats["power"] += 1
            level -= 1
        elif skill in ["s", "speed"]:
            stand_stats["speed"] += 1
            level -= 1
        elif skill in ["r", "range"]:
            stand_stats["range"] += 1
            level -= 1
        elif skill in ["st", "stamina"]:
            stand_stats["stamina"] += 1
            level -= 1
        elif skill in ["pr", "precision"]:
            stand_stats["precision"] += 1
            level -= 1  
        elif skill in ["po", "potential"]:
            stand_stats["potential"] += 1
            level -= 1
        elif skill in ["v", "vitality"]:
            stand_stats["vitality"] += 1
            level -= 1
        else:
            print("points left:", level)
            if level == 0:
                break
        
    return stand_stats #, level

#creating while loop to add lost entries to stats
def point_placement():
    while level > 0:
        print(level_up())

point_placement()

