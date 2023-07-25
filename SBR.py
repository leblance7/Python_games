#SBR Stand Class
#1)Creates a classes that can pull the stats of a stand from and allows modfication without
# altering the keys of a dictionary

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

#creation of instance variable for sbr

##    def __init__(self,
##                 power = 0,
##                 speed = 0,
##                 Range = 0,
##                 stamina = 0,
##                 precision = 0,
##                 potential = 0,
##                 vitality = 0):
##        self.power = power
##        self.speed = speed
##        self.Range = Range
##        self.stamina = stamina
##        self.precision = precision
##        self.potential = potential
##        self.vitality = vitality
##    def get_stats(self):
##        print("power:", self.power, "speed:", self.speed, "range:", self.Range,
##              "stamina:", self.stamina, "precision:", self.precision, "potential:",
##              self.potential, "vitality:", self.vitality)
##    def stats(self):
##        stats = []
##        stats.append(self.power)
##        stats.append(self.speed)
##        stats.append(self.Range)
##        stats.append(self.vitality)
##        return stats
##
##stat = SBR()
##stat = stat.stats()
##print(stat)
