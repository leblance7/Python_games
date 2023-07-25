#steel_ball_run
#1) Imports a class called SBR from SBR.py
#2) Create a function that allows the user to customize their character stats
#   and distrubute while leveling up, also create continous loop for misplaced stats
#3) Create a generator for enemy stands usings the stats variable

from dataclasses import dataclass

@dataclass 
class SBR:
    power: int = 0
    speed: int = 0
    Range: int = 0
    stamina: int = 0
    precision: int = 0
    potential: int = 0
    vitality: int = 0

import random
stat = SBR()
level = 3
persona = input("Enter the name of your stand: ")

def level_up():
    global level

    # call the class and assign it to stats
    # creates loop using skill to determine which stats your points go into,
    # resets loop with corrected number to distrubte points class variables
    for x in range(level):
        print("You have", level, "points left!")
        skill = input(
            "Choose from power, p, speed, s, range, r ,stamina, st, \n"
            + "precision, pr, potential, po, or vitality v: "
            ).lower()
        print(skill)
        if skill in ["p", "power"]:
            stat.power += 1
            level -= 1
            print("power")
        elif skill in ['s', 'speed']:
            stat.speed += 1
            level -= 1
            print("speed")
        elif skill in ["r", "range"]:
            stat.Range += 1
            level -= 1
            print("range")
        elif skill in ["st", "stamina"]:
            stat.stamina += 1
            level -= 1
            print("stamina")
        elif skill in ["pr", "precision"]:
            stat.precision += 1
            level -= 1
            print("precision")
        elif skill in ["po", "potential"]:
            stat.potential += 1
            level -= 1
            print("potential")
        elif skill in ["v", "vitality"]:
            stat.vitality += 1
            level -= 1
            print("vitality")
        else:
            print("Points left:", level)
            if level == 0:
                break
    return stat

#function for misinputed points that recalls the level_up() with the updated level

def point_placement():
    while level > 0:
        stand = level_up()
    return stand
        
def enemies():
    enemies = ["strong", "quick", "tough"]
    encounter = random.choice(enemies)
    enemy_stand = SBR()
    # Determin the different stats for enemies
    if encounter == "strong":
        enemy_stand.power += random.randint(1, 3)
        enemy_stand.speed += random.randint(0, 2)
        enemy_stand.Range += random.randint(0, 1)
        enemy_stand.stamina += random.randint(0, 1)
        enemy_stand.precision += random.randint(0, 1)
        enemy_stand.potential += random.randint(0, 1)
        enemy_stand.vitality += random.randint(0,3)
    elif encounter == "quick":
        enemy_stand.power += random.randint(0, 1)
        enemy_stand.speed += random.randint(1, 3)
        enemy_stand.Range += random.randint(0, 1)
        enemy_stand.stamina += random.randint(0, 2)
        enemy_stand.precision += random.randint(0, 2)
        enemy_stand.potential += random.randint(0, 1)
        enemy_stand.vitality += random.randint(0,2)
    elif encounter == "tough":
        enemy_stand.power += random.randint(0, 2)
        enemy_stand.speed += random.randint(0, 1)
        enemy_stand.Range += random.randint(0, 2)
        enemy_stand.stamina += random.randint(0, 1)
        enemy_stand.precision += random.randint(0, 2)
        enemy_stand.potential += random.randint(0, 1)
        enemy_stand.vitality += random.randint(1,3)
    return enemy_stand, encounter

##def moves_first(stand, enemy_stand):
    
# character.speed >enemy.speed:
# print(character moves first)

def moves_first():
    if stand.speed > enemy_stand.speed:
        print("You move first")
        print("<====================>")
        outcome = persona
        return outcome
    elif stand.speed < enemy_stand.speed:
        print("Encounter moves first,")
        print("<====================>")
        outcome = encounter
        return outcome
    elif stand.speed == enemy_stand.speed:
        print( "You and encounter tied.")
        priority = [stand, enemy_stand]
        priority = random.choice(priority)
        if priority == stand:
            print("Your stand barely moves first.")
            print("<====================>")
            outcome = persona
            return outcome
        elif priority == enemy_stand:
            print("Encounter barely moved first.")
            print("<====================>")
            priority = [enemy_stand, stand]
            outcome  = encounter
            return outcome

#Assigning values from function into variables
enemy_stand, encounter = enemies()
stand = point_placement() 
print("Stand:", stand)
print("Encounter:", encounter, '\n'+ str(encounter) + ":", enemy_stand)


outcome = moves_first()


#1) Imports a class called SBR from SBR.py
#2) Create a function that allows the user to customize their character stats
#   and distrubute while leveling up, also create continous loop for misplaced stats
#3) Create a generator for enemy stands usings the stats variable
# call the class and assign it to stats
    # creates loop using skill to determine which stats your points go into,
    # resets loop with corrected number to distrubte points class variables
#function for misinputed points that recalls the level_up() with the updated level
# Determin the different stats for enemies
#Assigning values from function into variables
