class Employee(object):  # create class for employee

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):  # create class that uses employee

    def __init__(self, name, number, shift, hourlypayrate):

        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__hourlypayrate = hourlypayrate

    def set_shift(self, shift):
        self.__shift = shift

    def set_hourlypayrate(self, hourlypayrate):
        self.__hourlypayrate = hourlypayrate

    def get_shift(self):
        return self.__shift

    def get_hourlypayrate(self):
        return self.__hourlypayrate
