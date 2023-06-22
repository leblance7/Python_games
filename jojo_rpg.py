#Character creation: includs stats list, what race the character will be, and weapons,
# armor, and weight


#stand stats are determined in range of e, e+, d, d+, c, c+, b, b+,a, and a+ going by increments of 10

##def player():
##    power = 0
##    speed = 0
##    Range = 0
##    durability = 0
##    precision = 0
##    potential = 0
##    stand_stats  = {
##        "power": power,
##        "speed": speed,
##        "range": Range,
##        "durability": durability,
##        "precision": precision,
##        "potential": potential    
##    }
##    return stand_stats

stand_name = input("What is the name of your stand: ")
stand_stats = {"power" : 0, "speed" : 0, "Range" : 0, "durability" : 0, "precision" : 0,
               "potential" : 0}
#creating a global variable that can be accessed within the function determining_stats()
#Creating function for variable level_up and to accumilate exp
exp = 0
level_up = 5
def exp():
    level_up = 5
    return level_up


def determining_stats(level_up):
    print("Where would you like to incease proficency?")
    #creating the for loop to determine stats of stand
    level_up = exp()
    
    for x in range(level_up):
        print(level_up, "start of loop")
        skill = input("Power, p, Speed, s, Range, r,\nDurability, d," +
                      " Precision, pr, or Potential, pp: ").lower()
        if skill in ['p', "power"]:
            stand_stats["power"] += 1
            level_up -= 1
            print(level_up)
        elif skill in ['s','speed']:
            stand_stats["speed"] += 1
            level_up -= 1
            print(level_up)
        elif skill in ['r', 'range']:
            level_up -= 1
            stand_stats["Range"] += 1
            print(level_up)
        elif skill in ['d', 'durability']:
            stand_stats['durability'] += 1
            level_up -= 1
            print(level_up)
        elif skill in ['pr', 'precision']:
            stand_stats["precision"] =+ 1
            level_up -= 1
            print(level_up)
        elif skill in ["pp", "potential"]:
            stand_stats["potential"] += 1
            level_up -= 1
            print(level_up)
        else:
#figuring out how to increase run through within loop
#subtract the from the range of the loop and recall the function
            print("Please pick a proficency that matches that choices listed.")
            print(level_up)
#while loop to reuse points that have been misentered
    while level_up > 0:
                print(level_up, "correction loop")
                print("Please reenter your stats: ")
                level_up = determining_stats(level_up)
    return stand_stats

#Creating level up as a local varaible

stand_stats, level_up = determining_stats(level_up)
             
##print(player())
