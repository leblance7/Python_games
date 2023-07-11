# STEELBALLRUN_rpg
# 1) To create a text based, stragety rpg game, that allows battles between charcters based
# on stats of a character build.
# 6-15-2022 start
# 2) A function that allows the placement of stats and uses the same function to
# to rename enemys the players will fight against
#3) Create different stats for enemies using the function enemies()
#4) Create a class for stats to call upon for characters
import random

stand_name = input("Enter the name of your stand: ")
##stand = {stand_name: stand_stats}

# shifting stand_stats into a function so the varible becomes local
def stand_stats(name: str) -> dict:
    stand_stats = {
        "power": 0,
        "speed": 0,
        "range": 0,
        "stamina": 0,
        "precision": 0,
        "potential": 0,
        "vitality": 0,
    }
    return stand_stats


# generating enemies for character to fight
def enemies():
    enemies = ["strong", "quick", "tough"]
    ##    for x in enemies:
    encounter = random.choice(enemies)
    stats = stand_stats(stand_name)
    #determing the differe stats of enemies for quick, strong, or tough
    #Based on stand Silver Chariot
    if encounter == "quick":
        stats["power"] += random.randint(0, 1)
        stats["speed"] += random.randint(1, 3)
        stats["range"] += random.randint(0, 1)
        stats["stamina"] += random.randint(0, 2)
        stats["precision"] += random.randint(0, 2)
        stats["potential"] += random.randint(0, 1)
        stats["vitality"] += random.randint(0, 2)

    #Based on stick fingers
    elif encounter == "strong":
        stats["power"] += random.randint(1, 3)
        stats["speed"] += random.randint(0, 2)
        stats["range"] += random.randint(0, 1)
        stats["stamina"] += random.randint(0, 1)
        stats["precision"] += random.randint(0, 1)
        stats["potential"] += random.randint(0, 1)
        stats["vitality"] += random.randint(0, 3)

    #Also based on sticky fingers
    elif encounter == "tough":
        stats["power"] += random.randint(0, 2)
        stats["speed"] += random.randint(0, 1)
        stats["range"] += random.randint(0, 2)
        stats["stamina"] += random.randint(0, 1)
        stats["precision"] += random.randint(0, 2)
        stats["potential"] += random.randint(0, 1)
        stats["vitality"] += random.randint(0, 3)
        
        
    enemy_stand = {encounter: stats}
    return enemy_stand, encounter


# creating variable for enemy_stand to be global

##enemy_stand = enemies()
##print(enemy_stand)


##print(stand)

level = 5

# level_up() alters the local varaible level to be gloabal, print statement
# Level_up uses the skill input statement in a for loop make a case statement determining
#  users stats in a dictionary


def level_up():
    stats = stand_stats(stand_name)

    global level
    print("Please enter the the stat you would like to increase.")

    # creating the for loop to determine which stats your points go into,
    # resets loop with corrected number to distrubte points and reuturn the updated dictionary

    for x in range(level):
        skill = input(
            "Choose from power, p, speed, s, range, r, stamina, st,\n"
            + "precision, pr, potential, po, or vitality, v: "
        ).lower()

        # conditional statements of where points will go based on skill input

        print(skill)
        if skill in ["p", "power"]:
            stats["power"] += 1
            level -= 1
        elif skill in ["s", "speed"]:
            stats["speed"] += 1
            level -= 1
        elif skill in ["r", "range"]:
            stats["range"] += 1
            level -= 1
        elif skill in ["st", "stamina"]:
            stats["stamina"] += 1
            level -= 1
        elif skill in ["pr", "precision"]:
            stats["precision"] += 1
            level -= 1
        elif skill in ["po", "potential"]:
            stats["potential"] += 1
            level -= 1
        elif skill in ["v", "vitality"]:
            stats["vitality"] += 1
            level -= 1
        else:
            print("points left:", level)
            if level == 0:
                break

    return stats  # , level


# creating while loop to add lost entries to stats
def point_placement():
    ##    stats = level_up()
    ##    print("stats", stats)
    while level > 0:
        stat = level_up()
    return stat
##        print("stats", stat)


stat = point_placement()
character = {stand_name: stat}
enemy_stand, encounter = enemies()
print(enemy_stand)
print(character)

#Creating a function that determines which character moves first & how to break a tie
# Check the random probabilty of moves first
def moves_first(character, enemy_stand):
    if character[stand_name]["speed"] > enemy_stand[encounter]["speed"]:
        print(stand_name, "moves first!")
        return character
    elif character[stand_name]["speed"] < enemy_stand[encounter]["speed"]:
        print(encounter, "moves first!")
        return enemy_stand
    elif character[stand_name]["speed"] == enemy_stand[encounter]["speed"]:
        priority = [character, enemy_stand]
        priority = random.choice(priority)
        if priority == character:
            print(stand_name, "is barely faster!")
            return priority
        elif priority == enemy_stand:
            print(encounter, "is barely faster!")
            return priority
         
    
print(moves_first(character, enemy_stand))
# creating new stand enentries for players to fight

##for x in stand:
##    print(x)
##    for x in stand["jojo"]:
##        print(x, stand_stats[x])



#from dataclasses import dataclass

#@dataclass
#class Stats:
    #power: int = 0
    #speed: int = 0
    #range: int = 0
