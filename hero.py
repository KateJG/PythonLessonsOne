class Hero():
    """" Class to Create a Hero for our Game """
    def __init__(self, name, level, race):
        """Initiate my hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """ Print all parameters of this Hero """
        description = (self.name + " Level is:  " + str(self.level) + ", Race is: " + self.race + ", Health is: " + str(self.health)).title()
        print(description)

    def level_up(self):
        """ Upgrade Hero Level """
#        += is self.level = self.level + 1
        self.level += 1

    def move(self):
        """ Start moving """
        print("Hero " + self.name + " started moving...")

    def set_health(self, new_health_level):
        self.health = new_health_level
#-----------------------------------------------------------------

#child class
class SuperHero(Hero):
    """Class to create a Super Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Use Magic"""
        self.magic -= 10

    def show_hero(self):
        """ Print all parameters of this Hero """
        description = (self.name + " Level is:  " + str(self.level) + ", Race is: " + self.race + ", Health is: " + str(self.health)).title() + ", Magic is: " + str(self.magic)
        print(description)



