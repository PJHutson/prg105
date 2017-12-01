from Office_Furniture import OfficeFurniture


class Desk(OfficeFurniture):
    def __init__(self, category, material, length, width, height, drawer_location, drawer_number, price):
        OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__drawer_location = drawer_location
        self.__drawer_number = drawer_number

    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def set_drawer_number(self, drawer_number):
        self.__drawer_number = drawer_number

    def get_drawer_location(self):
        return self.__drawer_location

    def get_drawer_number(self):
        return self.__drawer_number

    def __str__(self):
        description = self.get_category() + " is made from " + self.get_material() + ", it is " \
                      + self.get_length() + " long, " + self.get_width() + " wide," + " and " + \
                        self.get_height() + " tall," + " with " + self.__drawer_number + " drawer(s) on " + self.__drawer_location + \
                      " side(s) " + " the cost is: " + format(self.get_price(), ".2f")
        return description


desk = Desk("Desk", "oak", "6 ft", "4 ft", "3 ft", "4", "both", 85.00)
